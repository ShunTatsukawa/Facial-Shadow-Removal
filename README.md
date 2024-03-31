<div align="center">
<h1>Facial Shadow Removal</h1>
</div>

![image](https://github.com/zhangbaijin/SpA-Former-shadow-removal/blob/main/attention-TWRNN.png)
# Qucikly run
## 1. TRAIN

Modify the `config.yml` to set your parameters and run:

```bash
python train.py
```

## 2. TEST

First，the dataset is trained on 256x256, so you should resize test dataset to 256x256, you can use the code to resize your image 
```bash python cascade.py```
and then follow the code to test the results:
```bash
python predict.py --config <path_to_config.yml_in_the_out_dir> --test_dir <path_to_a_directory_stored_test_data> --out_dir <path_to_an_output_directory> --pretrained <path_to_a_pretrained_model> --cuda
```
Attention visual results is bellow:[Attention visual results](https://drive.google.com/file/d/188MbZxi3rVB41vAzLX2dssW4sRLYLqyn/view?usp=sharing).

There're my pre-trained models on [ISTD](./pretrained_models/RICE1/)(`./pretrained_models/ISTD/gen_model_epoch_200.pth`) 

![image](https://github.com/zhangbaijin/SpA-Former-shadow-removal/blob/main/imgs/introduction.png)

## 3. Pretrained model

Download the pretrained model shadow-removal  [Google-drive](https://drive.google.com/drive/folders/1pxwwAfwnGKkLj-GAlkVCevbEQM4basgR?usp=sharing)
 and [Baidu Drive](https://pan.baidu.com/s/1slny1G_9WuxBcoyw5eKUVA)  提取码：rpis
## 4.Test results
Our test results:  [Google-drive](https://drive.google.com/file/d/1m-zE9wxiEL8lO8pX5n65cbi0GQaAGSPr/view?usp=sharing)
and [Baidu drive](https://pan.baidu.com/s/1ek9qaowfPg4CkDaZF6KTCQ)  提取码：18ut

## 5.Evaluate 
To reproduce PSNR/SSIM/RMSE scores of the paper, run MATLAB script
```
evaluate.m
```
In this section, I compares SpA-Former with several methods using peak signal to noise ratio (***PSNR***) and structural similarity index (***SSIM***)  and (***RMSE***) as metrics on datasets ISTD.

![image](https://github.com/zhangbaijin/Spatial-Transformer-shadow-removal/blob/main/compare.jpg))

# ACKNOLAGEMENT
The code is updated on [https://github.com/Penn000/SpA-GAN_for_cloud_removal)]

# 2. DATASET

## 2.1. ISTD_DATASET

Click [official address]([here](https://github.com/nhchiu/Shadow-Removal-ISTD)) Build the file structure as the folder `data` shown. Here `input` is the folder where the shadow image is stored and the folder `target` stores the corresponding no shadow images.

```
./
+-- data
    +--	ISTD_DATASET
        +-- train
        |   +-- input
        |   |   +-- 0.png
        |   |   +-- ...
        |   +-- target
        |       +-- 0.png
        |       +-- ...
        +-- test
            +-- input
            |   +-- 0.png
            |   +-- ...
            +-- target
                +-- 0.png
                +-- ...
```


##  CONTACT

Contact me if you have any questions about the code and its execution.

E-mail: framebreak@sjtu.edu.cn

If you think this work is helpful for your research, give me a star :-D

### Citations
```
@INPROCEEDINGS{10191081,
  author={Zhang, Xiaofeng and Zhao, Yudi and Gu, Chaochen and Lu, Changsheng and Zhu, Shanying},
  booktitle={2023 International Joint Conference on Neural Networks (IJCNN)}, 
  title={SpA-Former:An Effective and lightweight Transformer for image shadow removal}, 
  year={2023},
  volume={},
  number={},
  pages={1-8},
  doi={10.1109/IJCNN54540.2023.10191081}}
```


