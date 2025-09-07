
# Hệ thống nhận dạng chữ số nguyên viết tay (0-10) sử dụng AI

Dự án nhận dạng chữ số viết tay sử dụng mạng nơ-ron tích chập (CNN) với TensorFlow/Keras, huấn luyện trên bộ dữ liệu MNIST kết hợp hơn 500 ảnh tự thu thập. Hệ thống cung cấp REST API Flask và giao diện web đơn giản cho phép tải ảnh kiểm tra, trích xuất điểm và cập nhật file Excel tự động. Độ chính xác mô hình đạt ~98%.

## Cấu trúc dự án

- `model_train.py`: Huấn luyện mô hình CNN nhận dạng chữ số (0-10) trên MNIST + ảnh tự thu thập.
- `main.py`: Dự đoán một ảnh chữ số đơn lẻ.
- `batch_predict.py`: Dự đoán hàng loạt ảnh trong thư mục `test_digits/`, lưu kết quả vào Excel.
- `app.py`: REST API Flask và giao diện web cho phép upload ảnh, trả về kết quả dự đoán, tự động cập nhật file Excel.
- `templates/index.html`: Giao diện web upload ảnh, xem kết quả.
- `bieu_do.py`: Vẽ biểu đồ lịch sử huấn luyện mô hình.
- `data_train/`: Ảnh huấn luyện tự thu thập (0-10).
- `test_digits/`: Ảnh kiểm tra mô hình.
- `digit_classifier_0_to_10.keras`: File mô hình đã huấn luyện.
- `ket_qua_du_doan.xlsx`: File Excel lưu kết quả dự đoán.
- `training_history.pkl`, `training_plot.png`: Lịch sử và biểu đồ huấn luyện.
- `requirements.txt`: Danh sách thư viện cần thiết.


## Cài đặt

1. Tạo và kích hoạt môi trường ảo (khuyến nghị):

```powershell
python -m venv .venv
.\.venv\Scripts\Activate
```

2. Cài đặt các thư viện cần thiết:

```bash
pip install -r requirements.txt
# hoặc nếu thiếu:
pip install tensorflow keras flask pandas openpyxl scikit-learn matplotlib natsort pillow werkzeug
```


## Hướng dẫn sử dụng

### 1. Huấn luyện mô hình

```bash
python model_train.py
```
> Mô hình sẽ được lưu thành `digit_classifier_0_to_10.keras`.

### 2. Xem biểu đồ huấn luyện

```bash
python bieu_do.py
```
> Biểu đồ lưu tại `training_plot.png`.

### 3. Dự đoán một ảnh đơn lẻ

Chỉnh sửa đường dẫn ảnh trong `main.py`, sau đó:

```bash
python main.py
```
> Kết quả sẽ in ra console.

### 4. Dự đoán hàng loạt

```bash
python batch_predict.py
```
> Kết quả lưu vào `ket_qua_du_doan.xlsx`.

### 5. Sử dụng REST API Flask & giao diện web

Chạy server Flask:

```bash
python app.py
```

Sau đó truy cập [http://localhost:5000](http://localhost:5000) để sử dụng giao diện web:
- Upload ảnh kiểm tra, xem kết quả dự đoán, kết quả sẽ tự động lưu vào file Excel.

#### Sử dụng API
Gửi POST request tới `/api/predict` với file ảnh:

```bash
curl -F "file=@duongdan/ten_anh.png" http://localhost:5000/api/predict
```
> Kết quả trả về dạng JSON: tên file và số dự đoán.


## Dữ liệu & Mô hình

- Dữ liệu: Kết hợp bộ MNIST (0-9) và >500 ảnh tự thu thập (0-10) trong `data_train/`.
- Mô hình: CNN (Keras/TensorFlow) gồm các lớp Conv2D, MaxPooling2D, Flatten, Dense, Dropout.
- Độ chính xác đạt ~98% trên tập kiểm tra.

## Đóng góp & Liên hệ

Mọi ý kiến đóng góp xin gửi về nhóm phát triển hoặc tạo issue trên repository.
