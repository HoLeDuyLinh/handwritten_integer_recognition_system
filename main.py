import tensorflow as tf
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import load_img, img_to_array
import numpy as np

# Load model đã train
model = load_model("digit_classifier_0_to_10.keras")

# Đường dẫn đến ảnh cần nhận dạng
image_path = r'D:\XLA\data_train\0\5.png'  # sửa lại đúng file bạn test

# Tiền xử lý ảnh: grayscale, resize, normalize
img = load_img(image_path, color_mode='grayscale', target_size=(28, 28))
img_array = img_to_array(img) / 255.0  # chuẩn hóa về [0, 1]
img_array = np.expand_dims(img_array, axis=0)  # thêm batch dimension

# Dự đoán
pred = model.predict(img_array)
predicted_class = np.argmax(pred)

# In kết quả
print(f"Dự đoán: {predicted_class}")
