import cv2
import matplotlib.pyplot as plt

def main():
    
    # path = "C:\\Users\\win10\\Desktop\\opencv\\standard_test_images"
    
    imgpath1 =   "house.tiff"
    imgpath2 =   "lake.tiff"
    
    img1 = cv2.imread(imgpath1, 1)
    img2 = cv2.imread(imgpath2, 1)
    
    img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2RGB)
    img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2RGB)
   
    
    plt.subplot(1, 2, 1)
    plt.imshow(img1)
    plt.title('Liquid Drop')
    plt.xticks([])
    plt.yticks([])

    plt.subplot(1, 2, 2)
    plt.imshow(img2)
    plt.title('Lena')
    plt.xticks([])
    plt.yticks([])
    
    plt.show()  
 
if __name__ == "__main__":
    main()