import pickle
import matplotlib.pyplot as plt

# 🔹 Tải lại lịch sử training từ file training_history.pkl
history_path = "training_history.pkl"

try:
    with open(history_path, "rb") as f:
        history = pickle.load(f)
    print("Lịch sử training đã được tải thành công!")
except FileNotFoundError:
    print("Không tìm thấy file lịch sử training!")
    exit()

# Vẽ biểu đồ
plt.figure(figsize=(12, 5))

# Accuracy
plt.subplot(1, 2, 1)
plt.plot(history['accuracy'], label='Train Acc')
plt.plot(history['val_accuracy'], label='Val Acc')
plt.title('Accuracy theo Epoch')
plt.xlabel('Epoch')
plt.ylabel('Accuracy')
plt.legend()

# Loss
plt.subplot(1, 2, 2)
plt.plot(history['loss'], label='Train Loss')
plt.plot(history['val_loss'], label='Val Loss')
plt.title('Loss theo Epoch')
plt.xlabel('Epoch')
plt.ylabel('Loss')
plt.legend()

plt.tight_layout()
plt.savefig("training_plot.png")
plt.show()
