import numpy as np
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense, Dropout
from tensorflow.keras.preprocessing.image import load_img, img_to_array
from tensorflow.keras.utils import to_categorical
import os
from sklearn.model_selection import train_test_split
import random

# Fix mọi loại random để mô hình đừng sống hai mặt
seed = 42
os.environ['PYTHONHASHSEED'] = str(seed)
random.seed(seed)
np.random.seed(seed)
tf.random.set_seed(seed)

# Load MNIST 0-9
(x_mnist, y_mnist), _ = tf.keras.datasets.mnist.load_data()
x_mnist = x_mnist.reshape(-1, 28, 28, 1) / 255.0
y_mnist = y_mnist.astype(np.int32)

# Load custom dataset (0-10)
def load_custom_images(data_dir):
    X, y = [], []
    for label in range(11):  # 0 đến 10
        folder = os.path.join(data_dir, str(label))
        if not os.path.isdir(folder):
            continue
        for file in os.listdir(folder):
            img_path = os.path.join(folder, file)
            img = load_img(img_path, target_size=(28,28), color_mode='grayscale')
            arr = img_to_array(img) / 255.0
            arr = arr.reshape(28, 28, 1)  # Đảm bảo đúng shape
            X.append(arr)
            y.append(label)
    X = np.array(X)
    return X, np.array(y, dtype=np.int32)

custom_dir = "data_train"
x_custom, y_custom = load_custom_images(custom_dir)

# Gộp 2 tập
x_all = np.concatenate((x_mnist, x_custom), axis=0)
y_all = np.concatenate((y_mnist, y_custom), axis=0)

# Shuffle & Split
x_train, x_val, y_train, y_val = train_test_split(x_all, y_all, test_size=0.2, random_state=42, stratify=y_all)

# Build model
from tensorflow.keras import Input
model = Sequential([
    Conv2D(32, (3,3), activation='relu', input_shape=(28,28,1)),
    MaxPooling2D(2,2),
    Conv2D(64, (3,3), activation='relu'),
    MaxPooling2D(2,2),
    Flatten(),
    Dense(128, activation='relu'),
    Dropout(0.3),
    Dense(11, activation='softmax')  # 11 lớp
])

model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

from tensorflow.keras.callbacks import EarlyStopping

# Tạo callback
early_stop = EarlyStopping(
    monitor='val_loss',
    patience=3,
    restore_best_weights=True
)

# Huấn luyện model
history = model.fit(
    x_train,
    y_train,
    validation_data=(x_val, y_val),
    epochs=20,               # Có thể đặt cao, vì nó sẽ dừng sớm
    batch_size=32,
    callbacks=[early_stop]
)

# Save model
model.save("digit_classifier_0_to_10.keras")

# Lưu lịch sử training
import pickle
with open("training_history.pkl", "wb") as f:
    pickle.dump(history.history, f)