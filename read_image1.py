import cv2
import time
import os

def main():
    path  = 'C:\\Users\\win10\\Desktop\\opencv\\standard_test_images\\'
    files = os.listdir(path)
    image_paths = []
    output_paths = []
    names = []


    output_path = 'C:\\Users\\win10\\Desktop\\opencv\\standard_test_images\\output'

    for file in files:

        image_paths.append(path+file)
        # file = (file[:-3])
        # print(file)

    print(names)

    for file in files:
        output_paths.append(output_path+file[:-3]+'jpg')
    
    print(output_paths)
    
    for image_path,output_path  in zip(image_paths,output_paths):

        img = cv2.imread(image_path)

        cv2.imshow('Lena',img)
        cv2.imwrite(output_path,img)

        # ouytput_path = os.getcwd()+'\\output1\\file'
        
        cv2.waitKey(100)    

if __name__ == "__main__":
    main()


