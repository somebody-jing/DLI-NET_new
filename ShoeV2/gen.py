import os


folder_path = "/data/zj/SBIR/DLI-Net-main/ShoeV2/trainB"


image_names = [file for file in os.listdir(folder_path) if file.endswith(('.jpg', '.png', '.jpeg', '.gif', '.bmp'))]


txt_file_path = "/data/zj/SBIR/DLI-Net-main/ShoeV2/photo_train.txt"
with open(txt_file_path, 'w') as txt_file:
    for image_name in image_names:
        txt_file.write(image_name + '\n')

