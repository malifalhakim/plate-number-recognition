import cv2
import numpy as np
from pathlib import Path
from PIL import Image
from straug.geometry import Shrink,Perspective,Rotate
from straug.camera import Contrast,Pixelate

# Load Image Train Path
train_image_path = Path("D:\Pemrograman\Data Science\SatriaData\Data Train ESRGAN")
train_image_path = list(train_image_path.glob("*.png"))
train_image_path = sorted(train_image_path, key=lambda path: int(path.stem.split("_")[0].split("DataTrain")[-1]))
train_image_path = list(map(str, train_image_path))
train_images = train_image_path

# Load Image Test Path
test_image_path = Path("D:\Pemrograman\Data Science\SatriaData\Data Test ESRGAN")
test_image_path = list(test_image_path.glob("*.png"))
test_image_path = sorted(test_image_path, key=lambda path: int(path.stem.split("_")[0].split("DataTest")[-1]))
test_image_path = list(map(str, test_image_path))
test_images = test_image_path

# Load Image Train Label Path
train_label_path = Path("D:\Pemrograman\Data Science\SatriaData\Image Processing\\train\labels")
train_label_path = list(train_label_path.glob("*.txt"))
train_label_path = sorted(train_label_path,key=lambda path: int(path.stem.split("_")[0].split("DataTrain")[-1]))
train_label_path = list(map(str,train_label_path))
train_label = train_label_path

# Load Image Test Label Path
test_label_path = Path("D:\Pemrograman\Data Science\SatriaData\Image Processing\\test\labels")
test_label_path = list(test_label_path.glob("*.txt"))
test_label_path = sorted(test_label_path,key=lambda path: int(path.stem.split("_")[0].split("DataTest")[-1]))
test_label_path = list(map(str,test_label_path))
test_label = test_label_path

def read_label(image_path,label_path):
    img = cv2.imread(image_path)
    with open(label_path) as f:
        annotations = f.readline()
    tokens = annotations.split(" ")
    if len(tokens) == 5:
        x_center = float(tokens[1])
        y_center = float(tokens[2])
        width = float(tokens[3])
        height = float(tokens[4])

        x_min = (x_center - width/2) * img.shape[1]
        x_max = (x_center + width/2) * img.shape[1]
        y_min = (y_center - height/2) * img.shape[0]
        y_max = (y_center + height/2) * img.shape[0]

        return [(x_min,y_max),(x_min,y_min),(x_max,y_min),(x_max,y_max)]
    
    x1 = float(tokens[1]) * img.shape[1]
    y1 = float(tokens[2]) * img.shape[0]
    x2 = float(tokens[3]) * img.shape[1]
    y2 = float(tokens[4]) * img.shape[0]
    x3 = float(tokens[5]) * img.shape[1]
    y3 = float(tokens[6]) * img.shape[0]
    x4 = float(tokens[7]) * img.shape[1]
    y4 = float(tokens[8]) * img.shape[0]

    return [(x2,y2),(x1,y1),(x4,y4),(x3,y3)]

def bird_view(image_path,points):
    img = cv2.imread(image_path)
    
    pts1 = np.float32([[points[0][0],points[0][1]],[points[1][0],points[1][1]],
                                [points[2][0],points[2][1]],[points[3][0],points[3][1]]])
    #print(pts1)
    width = 200
    height = 50
    pts2 = np.float32([[0,height],[0,0],[width,0],[width,height]])
    matrix = cv2.getPerspectiveTransform(pts1,pts2)
    img_output = cv2.warpPerspective(img,matrix,(width,height))

    return img_output


# For checking

'''
points = read_label(test_images[0],test_label[0])
print(points)
cropped_image = bird_view(test_images[0],points)
cv2.imshow('a',cropped_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
'''

# Produce bird view for train
'''
for i in range(len(train_images)):
    points = read_label(train_images[i],train_label[i])
    bird_image = bird_view(train_images[i],points)
    cv2.imwrite(f"D:\Pemrograman\Data Science\SatriaData\Image Processing\\train_result\DataTrain{i+1}_rlt.png",bird_image)
    print(f"Gambar-{i+1} Berhasil DiProses")
'''

# Produce bird view for test
for i in range(len(test_images)):
    if i == 75:
        points = read_label(test_images[i],test_label[i])
        bird_image = bird_view(test_images[i],points)
        cv2.imwrite(f"D:\Pemrograman\Data Science\SatriaData\Image Processing\\test_result\DataTest{i+1}_rlt.png",bird_image)
        print(f"Gambar-{i+1} berhasil diproses")