import cv2
import numpy as np

def matchinMapConvolve(img,template,dest,_i,_j):
    rows, cols = template.shape

    for i in range(cols):
        for j in range(rows):
            dest[_i,_j] += np.square(int(template[i,j])-int(img[_i+i,_j+j]))

def matchingMap(img, template):
    rows,cols = img.shape
    trows,tcols = template.shape
    matching_map = np.zeros((rows-trows+1,cols-tcols+1))
    mrows, mcols = matching_map.shape

    for i in range(mrows):
        for j in range(mcols):
            matchinMapConvolve(img,template,matching_map,i,j)

    matching_map /= matching_map.max()
    matching_map *= 255
    return matching_map



def GetTheInputs():
    inputImg = input("Input image: ")
    targetImg = input("Target image: ")
    threshold = input("Detection threshold: ")
    return inputImg, targetImg, threshold

if __name__ == '__main__':
    #inpt, tgt, thrshd = GetTheInputs()
    #print(inpt)
    #print(tgt)
    #print(thrshd)

    grayInputImg = cv2.imread("img1.png", cv2.IMREAD_GRAYSCALE)
    #colorInputImg = cv2.imread(inpt, cv2.IMREAD_ANYCOLOR)
    grayTargetImg = cv2.imread("t1-img1.png", cv2.IMREAD_GRAYSCALE)
    #colorTargetImg = cv2.imread(tgt, cv2.IMREAD_ANYCOLOR)

    matching_map = matchingMap(grayInputImg,grayTargetImg)


    cv2.imshow("Matching Map", np.uint8(matching_map))
    cv2.waitKey(0)

