import os

'''
统计训练集验证集中有效标签数
Train:2636
Val:292
'''

train_image_dir='data/train/images'
train_image_label='data/train/labels'
val_image_dir='data/val/images'
val_image_label='data/val/labels'

train_imgs,train_labels=[],[]
for idx in range(len(os.listdir(train_image_dir))):
    try:
        train_imgs.append(os.listdir(train_image_dir)[idx][:-4])
        train_labels.append(os.listdir(train_image_label)[idx][:-4])
    except IndexError as e:
        print(os.listdir(train_image_dir)[idx])


val_imgs,val_labels=[],[]
for idx in range(len(os.listdir(val_image_dir))):
    try:
        val_imgs.append(os.listdir(val_image_dir)[idx][:-4])
        val_labels.append(os.listdir(val_image_label)[idx][:-4])
    except Exception as e:
        print(e)

train_num,val_num=0,0
for img in train_imgs:
    if img in train_labels:
        train_num+=1

for img in val_imgs:
    if img in val_labels:
        val_num+=1

print('Train:{}\n Val:{}'.format(train_num,val_num))

