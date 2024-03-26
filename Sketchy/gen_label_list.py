import os
import random

dataset_dir_train = '/data/zj/SBIR/DLI-Net-main/Sketchy/photo/tx_000100000000/train/'
dataset_dir_test = '/data/zj/SBIR/DLI-Net-main/Sketchy/photo/tx_000100000000/test/'
train_file = '/data/zj/SBIR/DLI-Net-main/Sketchy/photo_train_relative_path.txt'
test_file = '/data/zj/SBIR/DLI-Net-main/Sketchy/photo_test_relative_path.txt'

with open(train_file, 'w') as train_txt, open(test_file, 'w') as test_txt:
    #
    for class_name in os.listdir(dataset_dir_train):
        class_path_train = os.path.join(dataset_dir_train, class_name)
        class_path_test = os.path.join(dataset_dir_test, class_name)
        if os.path.isdir(class_path_train):
            images_train = os.listdir(class_path_train)
            train_images = images_train
        if os.path.isdir(class_path_test):
            images_test = os.listdir(class_path_test)
            test_images = images_test


            for img_name in train_images:
                img_path = os.path.join(class_name, img_name)
                train_txt.write(img_path + '\n')

            # 10

            for img_name in test_images:
                img_path = os.path.join(class_name, img_name)
                test_txt.write(img_path + '\n')
