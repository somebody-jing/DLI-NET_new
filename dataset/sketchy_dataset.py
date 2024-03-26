import torch
from torch.utils.data import Dataset
from torchvision import transforms
from PIL import Image
import random
import os
import numpy as np
from glob import glob


class TrainDataset(Dataset):
    def __init__(self,
                 ph_root,
                 sk_root,
                 ph_name_txt,
                 dict_path):
        norm = transforms.Normalize([0.5, 0.5, 0.5], [0.5, 0.5, 0.5])
        with open(ph_name_txt, 'r') as f:
            self.ph_paths = f.read().splitlines()

        self.ph_root = ph_root
        self.sk_root = sk_root
        self.transform = transforms.Compose([
            transforms.Resize(256),
            transforms.ToTensor(), norm
        ])
        self.label_dict = np.load(dict_path, allow_pickle=True).item()

    def __getitem__(self, index):
        ph_path = self.ph_paths[index]
        # ph_path= tree/n12523475_394.jpg
        #print("ph_path=", ph_path)
        ph_full_path = os.path.join(self.ph_root, ph_path) # ph_full_path =  /data/zj/SBIR/DLI-Net-main/Sketchy/photo/tx_000100000000/tree/n12523475_394.jpg

        #print("ph_full_path = ", ph_full_path)
        ph = Image.open(ph_full_path)
        ph = self.transform(ph)
        ph_class_name = ph_path.split('/')[0]
        #ph_class_name =  tree
        #print("ph_class_name=", ph_class_name)
        ph_class = torch.tensor(self.label_dict[ph_class_name])

        label = ph_path.split('/')[-1].split('.')[0] #label  = n04587559_8710
        #print("label", label)
        # sk_regex = /data/zj/SBIR/DLI-Net-main/Sketchy/sketch/tx_000100000000/train
        sk_regex = os.path.join(self.sk_root, 'train')
        sk_regex = self.sk_root
        #print("sk_regex", sk_regex)
        # sk_regex = /data/zj/SBIR/DLI-Net-main/Sketchy/sketch/tx_000100000000/train/n07695742_1237.jpg
        sk_regex = os.path.join(sk_regex, ph_class_name)
        #print("sk_regex_fin = ", sk_regex)
        #sk_regex = /data/zj/SBIR/DLI-Net-main/Sketchy/sketch/tx_000100000000/train/n07695742_1237.jpg/n07695742_1237-*
        sk_regex = os.path.join(sk_regex, label + '-*')
        #print("sk_regex22222= ", sk_regex)
        sk_paths = glob(sk_regex)
        #print("sk_paths11111111 = ", sk_paths)
        # if not sk_paths:
        #     print(f"No files found at {sk_regex}")
        # else:
        #     sk_path = sk_paths[0]
        #     print("sk_path:", sk_path)

        random.shuffle(sk_paths)
        sk_path = sk_paths[0]
        #print("sk_path:", sk_path)

        sk = Image.open(sk_path)
        sk = self.transform(sk)
        return ph, sk, ph_class

    def __len__(self):
        length = len(self.ph_paths)
        return length


class TestPhDataset(Dataset):
    def __init__(self, ph_root, ph_txt):
        self.ph_root = ph_root
        with open(ph_txt) as f:
            self.ph_names = f.read().splitlines()
        norm = transforms.Normalize(mean=[0.5, 0.5, 0.5], std=[0.5, 0.5, 0.5])
        self.transform = transforms.Compose(
            [transforms.Resize(256),
             transforms.ToTensor(), norm])

    def __getitem__(self, index: int):
        ph_name = self.ph_names[index]
        ph_label = ph_name.split('.')[0]
        ph_path = os.path.join(self.ph_root, ph_name)
        ph = Image.open(ph_path)
        ph = self.transform(ph)

        return ph, ph_label

    def __len__(self):
        return len(self.ph_names)


class TestSkDataset(Dataset):
    def __init__(self, sk_root, sk_txt):
        self.sk_root = sk_root
        with open(sk_txt) as f:
            self.sk_names = f.read().splitlines()
        norm = transforms.Normalize(mean=[0.5, 0.5, 0.5], std=[0.5, 0.5, 0.5])
        self.transform = transforms.Compose(
            [transforms.Resize(256),
             transforms.ToTensor(), norm])

    def __getitem__(self, index: int):
        sk_name = self.sk_names[index]
        sk_label = sk_name.split('.')[0]
        sk_path = os.path.join(self.sk_root, sk_name)
        sk = Image.open(sk_path)
        sk = self.transform(sk)

        return sk, sk_label

    def __len__(self):
        return len(self.sk_names)