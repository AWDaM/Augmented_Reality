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


    return matching_map

def checkForMatchesAndDrawRectangles(matching_map,threshold, image, target):
    counter = 0
    rows,cols = matching_map.shape
    target_rows, target_cols = target.shape

    for i in range(0,rows):
        for j in range(0,cols):
            if matching_map[i,j]/matching_map.max() <= threshold:
                cv2.rectangle(image, (j,i),(j+target_cols,i+target_rows), (0, 255, 0),2)
                counter += 1

    imgFound = np.zeros((40,300,3),np.uint8)
    font = cv2.FONT_HERSHEY_SIMPLEX

    if counter == 0:
        cv2.putText(imgFound, "TARGET NOT FOUND", (5, 30), font, 1, (0, 255, 0), 1)

    else:
        cv2.putText(imgFound,"TARGET FOUND",(5,30), font, 1, (0,255,0),1)

    cv2.imshow("Result", imgFound)



def GetTheInputs():
    inputImg = input("Input image: ")
    targetImg = input("Target image: ")
    threshold = input("Detection threshold: ")
    return inputImg, targetImg, threshold

if __name__ == '__main__':
    inpt, tgt, threshold = GetTheInputs()
    threshold = float(threshold)
    print(inpt)
    print(tgt)
    print(threshold)

    grayInputImg = cv2.imread(str(inpt), cv2.IMREAD_GRAYSCALE)
    colorInputImg = cv2.imread(str(inpt), cv2.IMREAD_ANYCOLOR)
    grayTargetImg = cv2.imread(str(tgt), cv2.IMREAD_GRAYSCALE)
    colorTargetImg = cv2.imread(str(tgt), cv2.IMREAD_ANYCOLOR)

    matching_map = matchingMap(grayInputImg,grayTargetImg)

    matching_map /= matching_map.max()
    matching_map *= 255

    checkForMatchesAndDrawRectangles(matching_map,threshold,colorInputImg,grayTargetImg)



    cv2.imshow("Image", np.uint8(colorInputImg))
    cv2.imshow("Target", np.uint8(colorTargetImg))
    cv2.imshow("Matching Map", np.uint8(matching_map))
    cv2.waitKey(0)

