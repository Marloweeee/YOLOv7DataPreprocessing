import os



def writeTxt(img_dir:str,path:str,train:bool):
    for idx,img in enumerate(os.listdir(img_dir)):
        with open('train.txt' if train else 'val.txt','a+') as f:
            f.write(path+img+'\n')
        print("当前已在{}中写入{}条信息".format('train' if train else 'val',idx+1))

if __name__ == '__main__':
    train_path = r'dataset/TrashDet/images/train/'
    val_path = r'dataset/TrashDet/images/val/'

    train_image_dir = 'data/train/images/'
    val_image_dir = 'data/val/images/'

    writeTxt(train_image_dir,train_path,True)
    writeTxt(val_image_dir,val_path,False)
