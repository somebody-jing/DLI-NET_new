import os
import shutil

def copy_selected_images(source_folder, txt_file, destination_folder):

    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)


    with open(txt_file, 'r') as file:
        selected_images = file.read().splitlines()


    for line in selected_images:
        category, filename = line.split('/')
        source_path = os.path.join(source_folder, category, filename)
        print("source_path",source_path)
        destination_path = os.path.join(destination_folder, category)
        if not os.path.exists(destination_path):
            os.makedirs(destination_path)
        #destination_path = os.path.join(destination_folder, filename)
        fin_path = os.path.join(destination_path, filename)
        print("destination_path", fin_path)


        if os.path.exists(source_path):
            shutil.copyfile(source_path, fin_path)



if __name__ == "__main__":
    source_folder = "/data/zj/SBIR/DLI-Net-main/Sketchy/photo_temp/tx_000100000000/"
    txt_file = "/data/zj/SBIR/DLI-Net-main/Sketchy/photo_test_relative_path.txt"
    destination_folder = "/data/zj/SBIR/DLI-Net-main/Sketchy/photo/tx_000100000000/test/"

    copy_selected_images(source_folder, txt_file, destination_folder)
