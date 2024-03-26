CUDA_VISIBLE_DEVICES=5 \
python train_v2.py \
    --ph_train_root /data/zj/SBIR/DLI-Net-main/ChairV2/trainB \
    --sk_train_root /data/zj/SBIR/DLI-Net-main/ChairV2/trainA \
    --ph_test_root /data/zj/SBIR/DLI-Net-main/ChairV2/testB \
    --sk_test_root /data/zj/SBIR/DLI-Net-main/ChairV2/testA \
    --ph_train_txt /data/zj/SBIR/DLI-Net-main/ChairV2/photo_train.txt \
    --ph_test_txt /data/zj/SBIR/DLI-Net-main/ChairV2/photo_test.txt \
    --sk_test_txt /data/zj/SBIR/DLI-Net-main/ChairV2/sketch_test.txt \
    --feature_type mid \
    --lr 0.0001 \
    --batch_size 32 \
    --epoch 100 \
    --margin 0.5 \
    --self_interaction \
    --cross_interaction \
    --k 0.5 \
    --norm_type 2norm \
    --result_dir /data/zj/SBIR/DLI-Net-main/ChairV2_result 