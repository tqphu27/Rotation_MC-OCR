@ -5,7 +5,7 @@ Trang chủ cuộc thi: https://rivf2021-mc-ocr.vietnlp.com/
**Cài đặt source code và thư viện**

```
cd mc_ocr
cd MC_OCR
pip3 install --upgrade pip
pip3 install -r requirements.txt
pip3 install -e .
```
```
cd text_detector/PaddleOCR
pip3 install -e .
python3 -m pip install paddlepaddle==2.0rc1 -i https://mirror.baidu.com/pypi/simple
```
```
cd text_classifier/vietocr
pip3 install -e .
```
## TASK 1: Đánh giá chất lượng hóa đơn
**Trainning:**
Chuẩn bị dữ liệu training giống như file *image_quality_evaluation/train.txt* và chạy
```
cd image_quality_evaluation
python3 train.py --train_mode=1 --path_file=train.txt  --img_size=640
