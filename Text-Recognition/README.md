# Text Recognition Modules 📝

This module uses pretrain PaddleOCR model that has been fine-tuned to predict the plate number on low-resolution images. 

### How to use 🚀 
1. Place images of low-res `plate image` that you want to recognize in `Dataset/Test` 📷
2. Run this command
    ```
    !python tools/infer_rec.py -c configs/rec/PP-OCRv3/en_PP-OCRv3_rec.yml -o Global.pretrained_model=./output/v3_en_mobile/iter_epoch201  Global.infer_img=./Dataset/Test
    ```
3. Result will be printed and saved in a txt file in `output/rec`
4. If you want to make a difference with the fine-tuned model OCR, learn this repository [PaddleOCR](https://github.com/PaddlePaddle/PaddleOCR) 🚀
