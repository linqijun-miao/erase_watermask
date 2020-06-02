import cv2
import os


def get_all(cwd):
    result=[]
    get_dir = os.listdir(cwd)
    for i in get_dir:
        sub_dir = os.path.join(cwd,i)
        if os.path.isdir(sub_dir):
            get_all(sub_dir)
        else:
            result.append(i)
    return result


def dewatermask(name):
    img = cv2.imread(name)
    height = img.shape[0]  
    width = img.shape[1]
    channels = img.shape[2]

    for row in range(height):  
        for col in range(width):  
            sum = int(img[row][col][0]) + int(img[row][col][1]) + int(img[row][col][2])
            if sum > 710:
                img[row][col][0] = 255
                img[row][col][1] = 255
                img[row][col][2] = 255
    cv2.imwrite(name, img)


dewater_print('zhi7.png')