from straug.warp import Curve,Stretch,Distort
from straug.geometry import Shrink,Perspective,Rotate
from straug.process import Solarize,Equalize,Invert,Sharpness,AutoContrast,Posterize
from straug.noise import GaussianNoise,SpeckleNoise,ImpulseNoise,ShotNoise
from straug.camera import Brightness,Pixelate,Contrast
from PIL import Image
import random
import cv2

train_number = 1

while train_number <= 640:
    PATH_DIR = f'D:\Pemrograman\Data Science\SatriaData\Image Processing\\train_result\DataTrain{train_number}_rlt.png'
    img = Image.open(PATH_DIR)

    rand = random.randint(1,8)
    
    if rand == 1:
        img = Brightness()(img,mag=3)
        print("Bright")
    elif rand == 2 or rand == 5 or rand == 6:
        img = Pixelate()(img,mag=3)
        print("Pixel")
    elif rand == 3:
        img = GaussianNoise()(img,mag=3)
        print("Gauss")
    else:
        img = Contrast()(img,mag=3)
        print("Contr")
    
    img.save(f'augmentation_result\DataTrain{1440+ train_number}_rlt.png')
    train_number += 1


