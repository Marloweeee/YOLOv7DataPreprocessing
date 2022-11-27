import os
import cv2

'''
将注释文件转换为yolo格式的训练文件
'''

label2int = {'banana': 0, 'CARDBOARD': 1, 'bottle': 2}


def convert(c, size, box):
    dw, dh = 1. / (size[0]), 1. / (size[1])
    x = round((box[0] + box[2]) * 0.5 * dw, 8)
    y = round((box[1] + box[3]) * 0.5 * dh, 8)
    w = round((box[2] - box[0]) * dw, 8)
    h = round((box[3] - box[1]) * dw, 8)
    return [c, x, y, w, h]


def annosNoormalize(train_image_label: str, train_image_dir: str, train_annos: str):
    for idx, img in enumerate(os.listdir(train_image_label)):
        # 得到图片和注释文件路径
        img_path = train_image_dir + img[:-4] + '.jpg'
        label_path = train_image_label + img

        # 读取图片得到图片尺寸信息:416*416 or 640*640
        image = cv2.imread(img_path)
        size = image.shape[:2]  # width,height

        # 读取注释文件得到bbox信息
        annos = []
        with open(label_path, 'rb') as f:
            # 文件读取内容为bytes类型字符串，需要用decode函数解码
            for line in f.readlines():
                line = line.decode().strip().split(' ')
                c = label2int[line[0]]  # 字符型标签转为整形标签
                bbox = list(map(float, line[4:8]))  # x_min, y_min, x_max, y_max
                anno = convert(c, size, bbox)
                annos.append(anno)

        # 将bbox信息写入到新注释文件
        with open(train_annos + img, 'a+') as f:
            for items in annos:
                for num, item in enumerate(items):
                    f.write(str(item) if num == 0 else ' ' + str(item))

                f.write('\n')
        print("当前已经处理完成{}的{}个注释文件".format(train_annos.split('_')[0], idx + 1))


if __name__ == '__main__':
    train_image_dir = 'data/train/images/'
    train_image_label = 'data/train/labels/'
    train_annos = 'train_labels/'

    val_image_dir = 'data/val/images/'
    val_image_label = 'data/val/labels/'
    val_annos = 'val_labels/'

    annosNoormalize(train_image_label, train_image_dir, train_annos)
    annosNoormalize(val_image_label, val_image_dir, val_annos)
