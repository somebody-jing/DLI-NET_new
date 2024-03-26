import os
import shutil

source_folder = "/data/zj/SBIR/DLI-Net-main/Sketchy/sketch_dataset/temp/tx_000100000000/"
destination_train_folder = "/data/zj/SBIR/DLI-Net-main/Sketchy/sketch/tx_000100000000/train/"
destination_test_folder = "/data/zj/SBIR/DLI-Net-main/Sketchy/sketch/tx_000100000000/test/"
target_file_name = "sketch_test_relative_path.txt"

# Read the list of target file names from the text file
with open(target_file_name, "r") as file:
    target_file_paths = [line.strip() for line in file.readlines()]

# Iterate through target file paths
for target_file_path in target_file_paths:
    source_path = os.path.join(source_folder, target_file_path)

    # Determine the destination folder based on the target file path
    destination_folder = destination_test_folder if target_file_path in target_file_paths else destination_train_folder

    # Create the destination folder if it doesn't exist
    relative_path = os.path.relpath(source_path, source_folder)
    destination_path = os.path.join(destination_folder, relative_path)
    os.makedirs(os.path.dirname(destination_path), exist_ok=True)

    # Move the file to the destination
    shutil.move(source_path, destination_path)

print(f"Files moved from {source_folder} to {destination_train_folder} and {destination_test_folder}")
