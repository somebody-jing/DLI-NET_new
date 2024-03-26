CUDA_VISIBLE_DEVICES=2 \
python train_sketchy.py \
    --ph_train_root /data/zj/SBIR/DLI-Net-main/Sketchy/photo/tx_000100000000/train \
    --sk_train_root /data/zj/SBIR/DLI-Net-main/Sketchy/sketch/tx_000100000000/train \
    --ph_test_root /data/zj/SBIR/DLI-Net-main/Sketchy/photo/tx_000100000000/test \
    --sk_test_root /data/zj/SBIR/DLI-Net-main/Sketchy/sketch/tx_000100000000/test \
    --ph_train_txt /data/zj/SBIR/DLI-Net-main/Sketchy/photo_train_relative_path.txt \
    --ph_test_txt /data/zj/SBIR/DLI-Net-main/Sketchy/photo_test_relative_path.txt \
    --sk_test_txt /data/zj/SBIR/DLI-Net-main/Sketchy/sketch_test_relative_path.txt \
    --dict_path /data/zj/SBIR/DLI-Net-main/Sketchy/label_dict.npy \
    --feature_type global \
    --lr 0.00001 \
    --batch_size 16 \
    --epoch 300 \
    --margin 0.1 \
    --k 0.5 \
    --norm_type 2norm \
    --trip_weight 48 \
    --cls_weight 1 \
    --result_dir /data/zj/SBIR/DLI-Net-main/results_sketchy
