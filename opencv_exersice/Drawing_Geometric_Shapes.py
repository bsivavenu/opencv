import cv2
import numpy as np

def main():
	img1 = np.zeros((512,512,3),np.uint8)

	cv2.Line()
	cv2.imshow('Lena',img1)
	cv2.waitKey(0)
	cv2.destoryWindow('Lena')

if __name__ == '__main__':
	main()