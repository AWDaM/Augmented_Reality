import cv2
import numpy as np

def mathingMap(img, template):
    rows,cols = img.shape
    trows,tcols = template.shape
    matching_map = np.zeros(rows-trows+1,cols-tcols+1)

def GetTheInputs():
    inputImg = input("Input image: ")
    targetImg = input("Target image: ")
    threshold = input("Detection threshold: ")
    return inputImg, targetImg, threshold

if __name__ == '__main__':
    inpt, tgt, thrshd = GetTheInputs()
    print(inpt)
    print(tgt)
    print(thrshd)

    grayInputImg = cv2.imread(inpt, cv2.IMREAD_GRAYSCALE)
    colorInputImg = cv2.imread(inpt, cv2.IMREAD_ANYCOLOR)
    grayTargetImg = cv2.imread(tgt, cv2.IMREAD_GRAYSCALE)
    colorTargetImg = cv2.imread(tgt, cv2.IMREAD_ANYCOLOR)

