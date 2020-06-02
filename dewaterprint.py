import cv2
import os

#lllll
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


def dewater_print(name):
    img = cv2.imread(name)
    height = img.shape[0]  # 将tuple中的元素取出，赋值给height，width，channels
    width = img.shape[1]
    channels = img.shape[2]

    for row in range(height):  # 遍历每一行
        for col in range(width):  # 遍历每一列for channel in range(channels):
            sum = int(img[row][col][0]) + int(img[row][col][1]) + int(img[row][col][2])
            if sum > 710:
                img[row][col][0] = 255
                img[row][col][1] = 255
                img[row][col][2] = 255
    cv2.imwrite(name, img)


dewater_print('zhi7.png')