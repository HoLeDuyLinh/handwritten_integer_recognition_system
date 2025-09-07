import os
import numpy as np
import tensorflow as tf
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import load_img, img_to_array
import pandas as pd
from natsort import natsorted

# Load model
model = load_model("digit_classifier_0_to_10.keras")

# Folder chứa ảnh test
test_folder = "test_digits"  # Đổi lại nếu cần

# Tạo danh sách kết quả
results = []

# Sắp xếp ảnh theo thứ tự tự nhiên (1.png → 10.png)
filenames = natsorted([f for f in os.listdir(test_folder) if f.endswith(".png") or f.endswith(".jpg")])

# Duyệt qua từng ảnh
for filename in filenames:
    path = os.path.join(test_folder, filename)
    img = load_img(path, color_mode='grayscale', target_size=(28, 28))
    img_array = img_to_array(img) / 255.0
    img_array = np.expand_dims(img_array, axis=0)

    pred = model.predict(img_array)
    predicted_class = np.argmax(pred)

    print(f"{filename} → Dự đoán: {predicted_class}")
    results.append({
        "Tên ảnh": filename,
        "Điểm dự đoán": predicted_class
    })

# Đường dẫn file Excel
output_excel = "ket_qua_du_doan.xlsx"

# Ghi vào file Excel (gộp nếu đã tồn tại)
try:
    if os.path.exists(output_excel):
        old_df = pd.read_excel(output_excel)
        new_df = pd.DataFrame(results)
        combined_df = pd.concat([old_df, new_df], ignore_index=True)
    else:
        combined_df = pd.DataFrame(results)

    combined_df.to_excel(output_excel, index=False)
    print(f"Đã lưu kết quả vào file: {output_excel}")
except PermissionError:
    print(f"Không thể ghi file vì đang mở '{output_excel}'. Hãy đóng file Excel rồi chạy lại.")
