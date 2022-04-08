import os

CONFIG_ROOT = os.path.dirname(__file__)

#Path output file
OUTPUT_ROOT = '/content/gdrive/MyDrive/MC_OCR/output'


def full_path(sub_path, file=False):
    path = os.path.join(CONFIG_ROOT, sub_path)
    if not file and not os.path.exists(path):
        try:
            os.makedirs(path)
        except:
            print('full_path. Error makedirs',path)
    return path


def output_path(sub_path):
    path = os.path.join(OUTPUT_ROOT, sub_path)
    if not os.path.exists(path):
        try:
            os.makedirs(path)
        except:
            print('output_path. Error makedirs',path)
    return path

gpu = '0'  # None or 0,1,2...

#file name trong thư mục mc_ocr/data.
dataset = 'predict_image'
# mc_ocr_train_filtered
# mc_ocr_private_test

# input data from organizer
raw_train_img_dir = full_path('data/predict_image')
raw_img_dir=full_path('data/{}'.format(dataset))

#detector
#Path file txt sau khi detector
det_out_txt_dir=full_path('/content/gdrive/MyDrive/MC_OCR/output/text_detector/predict_image/txt')

# rotation corrector  
rot_drop_thresh = [.5, 2]
rot_visualize = True
#File weights
rot_model_path = full_path('rotation_corrector/weights/mobilenetv3-Epoch-487-Loss-0.03-Acc-0.99.pth', file=True)

#output 
rot_out_img_dir = output_path('rotation_corrector/{}/imgs'.format(dataset))
rot_out_txt_dir = output_path('rotation_corrector/{}/txt'.format(dataset))
rot_out_viz_dir = output_path('rotation_corrector/{}/viz_imgs'.format(dataset))
