import cv2
import time
import os

def main():
    path  = 'C:\\Users\\win10\\Desktop\\opencv\\standard_test_images\\'
    files = os.listdir(path)
    image_paths = []
    for file in files[:1]:
        image_paths.append(path+file)

    # print(image_paths)
    
    for image_path  in image_paths:

        img = cv2.imread(image_path,1)
        # ouytput_path = os.getcwd()+'\\output1\\file'
        print((img).dtype)
        print((img).shape, '....', img.size)

        cv2.imshow('Lena',img)
        cv2.waitKey(100)    

if __name__ == "__main__":
    main()

