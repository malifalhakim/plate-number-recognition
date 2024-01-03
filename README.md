# 🚗 Plate Number Recognition 📸

This project is a plate number recognition system that consists of three modules: ESRGAN, Image Processing, and Text-Recognition.

## 🖼️ ESRGAN

The ESRGAN module is used to enhance image resolution using a super resolution algorithm. It takes low-resolution images as input and produces high-resolution images as output.

## 📷 Image Processing

The Image Processing module is responsible for preprocessing images before training or prediction. It includes operations such as cropping, resizing, and applying filters to improve the quality of the images.

## 📝 Text-Recognition

The Text-Recognition module utilizes OCR (Optical Character Recognition) techniques to extract text from images. It uses a fine-tuned PaddleOCR model to accurately recognize and extract the plate numbers from the processed images.

## 🚀 Getting Started

To get started with this project, follow these steps:

1. Clone the repository.
2. Install the required dependencies.
3. Run the ESRGAN module to enhance the image resolution.
4. Preprocess the images using the Image Processing module.
5. Use the Text-Recognition module to perform OCR on the processed images and extract the plate numbers.

## 🔗 References

- [ESRGAN](https://github.com/xinntao/ESRGAN)
- [PaddleOCR](https://github.com/PaddlePaddle/PaddleOCR)
