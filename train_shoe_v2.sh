CUDA_VISIBLE_DEVICES=3 \
python train_v2.py \
    --ph_train_root /data/zj/SBIR/DLI-Net-main/ShoeV2/trainB \
    --sk_train_root /data/zj/SBIR/DLI-Net-main/ShoeV2/trainA \
    --ph_test_root  /data/zj/SBIR/DLI-Net-main/ShoeV2/testB \
    --sk_test_root  /data/zj/SBIR/DLI-Net-main/ShoeV2/testA \
    --ph_train_txt /data/zj/SBIR/DLI-Net-main/ShoeV2/photo_train.txt \
    --ph_test_txt /data/zj/SBIR/DLI-Net-main/ShoeV2/photo_test.txt \
    --sk_test_txt /data/zj/SBIR/DLI-Net-main/ShoeV2/sketch_test.txt \
    --feature_type mid \
    --lr 0.0001 \
    --batch_size 20 \
    --epoch 100 \
    --margin 0.1 \
    --self_interaction \
    --cross_interaction \
    --k 0.5 \
    --norm_type 2norm \
    --result_dir /data/zj/SBIR/DLI-Net-main/results