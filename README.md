# Hệ thống nhận dạng chữ số viết tay (0-10)

Đây là một dự án nhận dạng chữ số viết tay sử dụng mạng nơ-ron tích chập (CNN) với TensorFlow và Keras. Dự án này có khả năng nhận dạng các chữ số từ 0 đến 10, mở rộng từ bộ dữ liệu MNIST tiêu chuẩn.

## Cấu trúc dự án

- `main.py`: Tập lệnh này được sử dụng để dự đoán một ảnh chữ số riêng lẻ.
- `model_train.py`: Chứa mã để xây dựng, huấn luyện và lưu mô hình CNN nhận dạng chữ số. Nó sử dụng cả bộ dữ liệu MNIST và tập dữ liệu tùy chỉnh.
- `batch_predict.py`: Thực hiện dự đoán hàng loạt trên các ảnh trong thư mục `test_digits` và lưu kết quả vào một file Excel.
- `bieu_do.py`: Tạo biểu đồ hiển thị lịch sử huấn luyện của mô hình (độ chính xác và độ mất mát) từ file `training_history.pkl`.
- `data_train/`: Thư mục chứa tập dữ liệu huấn luyện tùy chỉnh, được tổ chức thành các thư mục con từ '0' đến '10' (mỗi thư mục chứa ảnh của chữ số tương ứng).
- `test_digits/`: Thư mục chứa các ảnh chữ số được sử dụng để kiểm tra mô hình.
- `digit_classifier_0_to_10.keras`: Mô hình CNN đã được huấn luyện.
- `ket_qua_du_doan.xlsx`: File Excel lưu trữ kết quả dự đoán từ `batch_predict.py`.
- `training_history.pkl`: File pickle chứa lịch sử huấn luyện của mô hình (độ chính xác và độ mất mát).
- `training_plot.png`: Ảnh biểu đồ thể hiện lịch sử huấn luyện của mô hình.
- `Nhom1_To6_Project_XLA.pptx`: Slide thuyết trình dự án.

## Cài đặt

Để chạy dự án này, bạn cần cài đặt các thư viện Python sau:

```bash
pip install tensorflow keras numpy scikit-learn pandas matplotlib natsort pillow
```

## Cách sử dụng

### 1. Huấn luyện mô hình

Chạy tập lệnh `model_train.py` để huấn luyện mô hình CNN:

```bash
python model_train.py
```

Mô hình đã huấn luyện sẽ được lưu dưới dạng `digit_classifier_0_to_10.keras` và lịch sử huấn luyện sẽ được lưu dưới dạng `training_history.pkl`.

### 2. Xem biểu đồ huấn luyện

Sau khi huấn luyện mô hình, bạn có thể xem biểu đồ độ chính xác và độ mất mát bằng cách chạy:

```bash
python bieu_do.py
```

Biểu đồ sẽ được lưu dưới dạng `training_plot.png` và hiển thị trên màn hình.

### 3. Dự đoán một ảnh đơn lẻ

Để dự đoán một ảnh chữ số, hãy chỉnh sửa đường dẫn ảnh trong `main.py` và sau đó chạy tập lệnh:

```bash
python main.py
```

Kết quả dự đoán sẽ được in ra console.

### 4. Dự đoán hàng loạt

Để chạy dự đoán trên tất cả các ảnh trong thư mục `test_digits` và lưu kết quả vào file Excel, hãy chạy:

```bash
python batch_predict.py
```

Kết quả sẽ được lưu vào file `ket_qua_du_doan.xlsx`. Nếu file đã tồn tại, kết quả mới sẽ được nối thêm vào.

## Tập dữ liệu

Dự án sử dụng kết hợp:
- Bộ dữ liệu MNIST (chữ số 0-9)
- Tập dữ liệu tùy chỉnh cho các chữ số từ 0-10, nằm trong thư mục `data_train/`.

## Mô hình

Mô hình là một mạng nơ-ron tích chập (CNN) được xây dựng bằng Keras, bao gồm các lớp `Conv2D`, `MaxPooling2D`, `Flatten`, `Dense` và `Dropout` để đạt được hiệu suất cao trong việc nhận dạng chữ số.
