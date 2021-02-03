## WT
## 2020.02.02
## VOC find train and test img

## 先使用划分好的VOC数据集将 训练测试图片放置不同的文件夹中，然后根据 train.txt 和 test.txt转成COCO json

import os, shutil

IMG_PATH = r'D:\VOCdevkit\VOCdevkit\VOC2007\JPEGImages'
IMG_TRAIN_SAVE_PATH = r'D:\VOCdevkit\VOCdevkit\VOC2007\instance_train'
IMG_VAL_SAVE_PATH = r'D:\VOCdevkit\VOCdevkit\VOC2007\instance_val'
TXT_TRAIN_PATH = r'D:\VOCdevkit\VOCdevkit\VOC2007\ImageSets\Main\train.txt'
TXT_VAL_PATH = r'D:\VOCdevkit\VOCdevkit\VOC2007\ImageSets\Main\val.txt'
train_txt = open(TXT_TRAIN_PATH, 'r', encoding='utf-8')

text = train_txt.readlines()
print('trian_data_num:',len(text))

val_txt = open(TXT_VAL_PATH, 'r', encoding='utf-8')
text_val = val_txt.readlines()
print('val_data_num:',len(text_val))

if not os.path.exists(IMG_TRAIN_SAVE_PATH):
    os.mkdir(IMG_TRAIN_SAVE_PATH)
    print('创建训练集图片文件')


if not os.path.exists(IMG_VAL_SAVE_PATH):
    os.mkdir(IMG_VAL_SAVE_PATH)
    print('创建VAL图片文件')


for i in text:
    shutil.copy(IMG_PATH + i[11:-1] + '.jpg', IMG_TRAIN_SAVE_PATH)
    # print(i)


for i in text_val:
    shutil.copy(IMG_PATH + i[11:-1] + '.jpg', IMG_VAL_SAVE_PATH)
    # print(i)




train_txt.close
val_txt.close
