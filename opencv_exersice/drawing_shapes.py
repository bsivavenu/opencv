import cv2
import numpy as np

def main():
	img1 = np.zeros((512,512,3),np.uint8)

	cv2.imread('Lena',img1)
	cv2.imshow()
	cv2.waitKey(0)

if __name__ == '__main__':
	main()