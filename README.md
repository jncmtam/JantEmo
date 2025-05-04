# Dự án Nhận diện Cảm xúc và Trạng thái Tinh thần bằng Computer Vision

## Mục tiêu Dự án

Dự án xây dựng một hệ thống sử dụng **Computer Vision** và **Machine Learning** để nhận diện cảm xúc (Disgust, Fear, Happy, Sad, Surprise, Neutral) và trạng thái tinh thần (tired, full_power) từ khuôn mặt qua webcam. Hệ thống được huấn luyện trên tập dữ liệu FER2013 và sử dụng mô hình CNN để dự đoán. Kết quả dự đoán được phân tích để tạo thông báo học tập (study alert) bằng giọng nói qua **Text-to-Speech (TTS)** của ElevenLabs, ví dụ: "You look tired. Maybe you should take a little rest." Dự án tập trung vào giai đoạn 1 để xây dựng nền tảng vững chắc về nhận diện cảm xúc, với tính năng kiểm tra xu hướng cảm xúc để thông báo một cách logic, tránh lặp lại không cần thiết.

---

## Kiến thức và Công nghệ Sử dụng

### Công nghệ
- **PyTorch**: Framework Deep Learning để xây dựng và huấn luyện CNN.
- **OpenCV**: Thư viện xử lý hình ảnh và luồng video từ webcam.
- **MediaPipe**: Thư viện phát hiện khuôn mặt thời gian thực, sử dụng mô hình BlazeFace.
- **ElevenLabs**: API Text-to-Speech để tạo thông báo bằng giọng nói.
- **Python Libraries**: Các thư viện hỗ trợ như `numpy`, `pandas`, `torchvision`, `mediapipe`.

### Kiến thức
1. **Computer Vision**:
   - Phát hiện và theo dõi khuôn mặt bằng MediaPipe Face Detection.
   - Tiền xử lý hình ảnh: Chuyển ảnh sang grayscale, chuẩn hóa và resize về kích thước 48x48.
   - Xử lý luồng video từ webcam để phân tích khuôn mặt theo thời gian thực.
2. **Deep Learning**:
   - Sử dụng Convolutional Neural Network (CNN) với kiến trúc đa đầu ra để dự đoán đồng thời cảm xúc và trạng thái tinh thần.
   - Huấn luyện mô hình trên FER2013 với hàm mất mát CrossEntropyLoss và tối ưu bằng Adam.
3. **Xử lý Dữ liệu**:
   - Tải và xử lý dữ liệu từ file CSV của FER2013.
   - Chia tập dữ liệu thành train/validation (80/20).
4. **Tích hợp TTS**:
   - Sử dụng API ElevenLabs để chuyển đổi văn bản thành giọng nói, cung cấp thông báo học tập dựa trên xu hướng cảm xúc.

---

## Cấu trúc Dự án

Dự án được tổ chức theo cấu trúc sau để đảm bảo tính mô-đun và dễ mở rộng:

- **assets/**: Chứa các file tĩnh (nếu có).
- **data/**: Chứa dữ liệu FER2013 (`fer2013.csv`).
- **env/**: Môi trường ảo Python.
- **logs/**: Nhật ký huấn luyện.
- **models/**: Chứa các mô hình đã huấn luyện (`emotion_mental_cnn.pth`).
- **output/**: Kết quả dự đoán hoặc file đầu ra.
- **src/**: Mã nguồn chính.
  - **models/**:
    - `cnn.py`: Định nghĩa mô hình CNN với 2 đầu ra (cảm xúc và trạng thái).
  - **utils/**:
    - `data_loader.py`: Tải và xử lý dữ liệu FER2013.
    - `face_utils.py`: Phát hiện và tiền xử lý khuôn mặt từ khung hình video bằng MediaPipe.
  - `train_emotion.py`: Script huấn luyện mô hình.
  - `predict.py`: Script dự đoán cảm xúc/trạng thái từ khung hình.
  - `interface.py`: Script chính tích hợp webcam, dự đoán, kiểm tra xu hướng cảm xúc, và TTS.
- **tests/**: Chứa các bài kiểm tra đơn vị.
- **README.md**: Tài liệu dự án.
- **requirements.txt**: Danh sách các thư viện cần thiết.
- **main.py**: Điểm nhập chính để chạy dự án.

---

## Cách Triển khai Dự án (Giai đoạn 1)

### 1. Chuẩn bị Môi trường
- Tạo môi trường ảo:
  ```bash
  python -m venv env
  ```
- Kích hoạt môi trường ảo:
  - Linux/Mac: `source env/bin/activate`
  - Windows: `env\Scripts\activate`
- Cài đặt các thư viện:
  ```bash
  pip install -r requirements.txt
  ```

### 2. Chuẩn bị Dữ liệu
- Tải tập dữ liệu FER2013 (file `fer2013.csv`) và đặt vào thư mục `data/`.
- File `fer2013.csv` chứa các cột: `emotion`, `pixels`, `Usage`.
- Nhãn cảm xúc trong FER2013: 0=Angry, 1=Disgust, 2=Fear, 3=Happy, 4=Sad, 5=Surprise, 6=Neutral. Dự án gộp Disgust và Neutral thành Neutral (5).
- Nhãn trạng thái tinh thần (tired, full_power) được giả định từ cảm xúc (Sad/Fear → tired, Happy/Surprise → full_power).

### 3. Huấn luyện Mô hình
- Chạy script huấn luyện:
  ```bash
  python src/train_emotion.py
  ```
- Mô hình sẽ được huấn luyện trong 10 epoch (có thể điều chỉnh) và lưu vào `models/emotion_mental_cnn.pth`.

### 4. Theo dõi qua Webcam và Tích hợp TTS
- Cài đặt biến môi trường cho ElevenLabs:
  ```bash
  export AGENT_ID=youragentid
  export ELEVENLABS_API_KEY=yourapikey
  ```
- Chạy dự án để theo dõi qua webcam:
  ```bash
  python main.py
  ```
- Quy trình hoạt động:
  1. Mở webcam và lấy khung hình video.
  2. Phát hiện khuôn mặt trong khung hình bằng MediaPipe Face Detection.
  3. Tiền xử lý ảnh khuôn mặt (grayscale, resize 48x48, chuẩn hóa).
  4. Dự đoán cảm xúc và trạng thái tinh thần bằng mô hình CNN.
  5. Lưu lịch sử cảm xúc và trạng thái, kiểm tra xu hướng cảm xúc (dựa trên ngưỡng 70% trong 60 khung hình gần nhất).
  6. Tạo câu thông báo phù hợp nếu cảm xúc/trạng thái đạt điều kiện và không trùng với thông báo trước.
  7. Gọi API ElevenLabs để chuyển văn bản thành giọng nói và phát audio.
  8. Thoát bằng cách nhấn phím `q`.

---

## Chi tiết Các Thành phần Chính

### 1. Mô hình CNN (`cnn.py`)
- **Kiến trúc**:
  - 3 tầng tích chập (Conv2d) với BatchNorm, ReLU, và MaxPooling.
  - Tầng fully connected chia sẻ, sau đó tách thành 2 đầu ra:
    - Đầu cảm xúc: Dự đoán 6 lớp (Disgust, Fear, Happy, Sad, Surprise, Neutral).
    - Đầu trạng thái: Dự đoán 2 lớp (tired, full_power).
- **Đầu vào**: Ảnh grayscale 48x48 (1 kênh).
- **Đầu ra**: Xác suất cho cảm xúc và trạng thái.

### 2. Tải và Xử lý Dữ liệu (`data_loader.py`)
- Đọc dữ liệu từ file `fer2013.csv`.
- Chuyển giá trị pixel thành tensor 48x48x1, chuẩn hóa.
- Chia dữ liệu thành tập train/validation.

### 3. Phát hiện và Theo dõi Khuôn mặt (`face_utils.py`)
- Sử dụng MediaPipe Face Detection (mô hình BlazeFace) để phát hiện khuôn mặt trong khung hình video.
- Tiền xử lý ảnh khuôn mặt để phù hợp với đầu vào của mô hình.

### 4. Dự đoán (`predict.py`)
- Tải mô hình đã huấn luyện.
- Dự đoán cảm xúc và trạng thái từ khung hình video.

### 5. Tích hợp Webcam và TTS (`interface.py`)
- Mở webcam và xử lý luồng video.
- Gọi dự đoán và kiểm tra xu hướng cảm xúc/trạng thái.
- Tạo và phát thông báo học tập bằng giọng nói qua ElevenLabs.

---

## Lưu ý và Hướng Phát triển

- **Tối ưu Hiệu suất**:
  - Thử nghiệm với các kiến trúc CNN khác (ResNet, MobileNet) để tăng độ chính xác.
  - Áp dụng data augmentation (xoay, thay đổi độ sáng) để cải thiện khả năng tổng quát hóa của mô hình.
- **Cải thiện Hệ thống**:
  - Điều chỉnh ngưỡng thông báo (`alert_threshold`) hoặc khoảng thời gian lịch sử (`history_length`) để phù hợp với nhu cầu.
  - Đánh giá mô hình bằng các chỉ số như accuracy, precision, recall để đo lường hiệu suất.
- **Kiểm tra**:
  - Viết thêm các bài kiểm tra đơn vị trong thư mục `tests/` để đảm bảo tính ổn định của mã nguồn.

---
