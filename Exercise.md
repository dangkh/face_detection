# Bài tập thực hành
Ở bài tập này anh/chị sẽ phải huấn luyện một bộ phân lớp phân tầng để phát hiện khuôn mặt. Anh/chị vẫn sử dụng Jupyter Notebook **`CascadeClassifierTraning.ipynb`** để huấn luyện. Tuy nhiên anh/chị phải căn chỉnh các tham số và thêm dữ liệu huấn luyện để đạt được mô hình tốt hơn.

## Thêm dữ liệu huấn luyện
Dữ liệu huấn luyện bao gồm các ảnh chứa khuôn mặt và các ảnh nền không chứa khuôn mặt. Một số lượng nhỏ ảnh huấn luyện đã được đặt trong hai thư mục **`data/input_positive`** và **`data/input_negative`**. Nhiệm vụ của anh/chị là thu thập thêm ảnh huấn luyện để đặt vào hai thư mục này.

- Ảnh positive là những ảnh chứa khuôn mặt được đặt trong thư mục **`data/input_positive`**

- Ảnh negative là những ảnh bất kỳ không chứa khuôn mặt được đặt trong thư mục **`data/input_negative`**.

## Căn chỉnh tham số huấn luyện
Anh/chị cần mở file **`train_cascade/config.py`** để căn chỉnh các tham số huấn luyện. Các tham số có thể căn chỉnh là:

- `WIDTH`:  chiều rộng của cửa sổ dịch
- `HEIGHT`: chiều cao của cửa sổ dịch
-  `MAX_NUM_POS`: số lượng ảnh positive tối đa để tạo vecfile (số lượng ảnh trong thư mục input_positive)
- `NUM_POS`: số lượng ảnh positive dùng để huấn luyện tại mỗi tầng (cần phải nhỏ hơn `MAX_NUM_POS`, nếu khi huấn luyện gặp lỗi, thử giảm `NUM_POS`)
- `NUM_NEG`:  số lượng ảnh negative dùng để huấn luyện tại mỗi tầng
- `NUM_STAGES`: số lượng tầng sẽ huấn luyện
- `MAX_FALSE_ALARM_RATE`:  Maximal desired false alarm rate for each stage of the classifier. Overall false alarm rate may be estimated as (max_false_alarm_rate ^ number_of_stages)
- `MIN_HIT_RATE`:  Minimal desired hit rate for each stage of the classifier. Overall hit rate may be estimated as (min_hit_rate ^ number_of_stages)
- `FEATURE_TYPE`:  Type of features: HAAR - Haar-like features, LBP - local binary patterns.
- `BOOST_TYPE`:  Type of boosted classifiers: DAB - Discrete AdaBoost, RAB - Real AdaBoost, LB - LogitBoost, GAB - Gentle AdaBoost.
- `EXTRA_PARAMS`: Các tham số khác, xem chi tiết tại [đây](http://docs.opencv.org/trunk/dc/d88/tutorial_traincascade.html).

## Lưu ý
Khi dùng file Jupyter Notebook **`CascadeClassifierTraning.ipynb`** để huấn luyện, sau khi sửa xong file **`config.py`**, code có thể chưa được update dẫn đến việc anh/chị huấn luyện lại model với tham số cũ. Để tránh việc đó, anh/chị có thể không dùng Jupyter Notebook để huấn luyện, thay vào đó chạy trực tiếp các file `.py` tại thư mục **`face_detection`**.

### Chuẩn bị dữ liệu
Chạy lệnh sau để chuẩn bị dữ liệu. Nếu không có thay đổi dữ liệu và `HEIGHT`, `WIDTH` của cửa sổ dịch thì chỉ cần chạy lệnh này lần đầu.
```bash
python prepare_samples.py
```

### Huấn luyện cascade classifier
Dùng lệnh sau để huấn luyện.
```bash
python train_cascade.py
```
