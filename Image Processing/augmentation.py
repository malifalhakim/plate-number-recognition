from PIL import Image
import random
import glob
# Can use any of the following augmentations:
from straug.warp import Curve,Stretch,Distort
from straug.geometry import Shrink,Perspective,Rotate
from straug.process import Solarize,Equalize,Invert,Sharpness,AutoContrast,Posterize
from straug.noise import GaussianNoise,SpeckleNoise,ImpulseNoise,ShotNoise
from straug.camera import Brightness,Pixelate,Contrast

no = 1
# Get a list of all png and jpg files in the directory
png_files = glob.glob('train/images/*.png') + glob.glob('train/images/*.jpg')
print(png_files)

for file in png_files:
    img = Image.open(file)

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
    
    # Save the image with a new name in a different directory
    new_file_name = f'augmentation_result\DataTrain{no}.png'
    img.save(new_file_name)
    no += 1


