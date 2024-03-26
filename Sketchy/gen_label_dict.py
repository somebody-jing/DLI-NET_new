import os
import numpy as np


def generate_label_dict(data_root):
    label_dict = {}

    # Traverse the dataset directory
    label_index = 0
    for class_name in os.listdir(data_root):
        class_path = os.path.join(data_root, class_name)

        # Process only folders
        if os.path.isdir(class_path):
            # Set label for each class folder, e.g., label for 'airplane' is 0
            label_dict[class_name] = label_index
            label_index += 1

    return label_dict


# Specify the dataset root directory
data_root = '/data/zj/SBIR/DLI-Net-main/Sketchy/photo/tx_000100000000'

# Generate the label dictionary
label_dict = generate_label_dict(data_root)

# Specify the custom path for the .npy file
custom_npy_path = '/data/zj/SBIR/DLI-Net-main/Sketchy/label_dict.npy'

# Save the label dictionary as a .npy file at the custom path
np.save(custom_npy_path, label_dict)
