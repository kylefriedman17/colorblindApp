# problems so far:
	# images need to have the same resolution
	# images with different color channels won't work#

from PIL import Image, ImageFile
from SSIM_PIL import compare_ssim
import cv2
import numpy as np
ImageFile.LOAD_TRUNCATED_IMAGES = True

# the two images go here


def main():
	img1 = cv2.imread('static/input.jpg')
	img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2RGB)
	img2 = cv2.imread('static/output.jpg')
	img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2RGB)
	return mse(img1, img2)

# compares images and returns percent difference
def compare_images(imageA, imageB):
	compare = compare_ssim(img1, img2)
	compare += 1
	compare = 2 - compare
	compare /= 2
	return compare * 100

def mse(imageA, imageB):
	# the 'Mean Squared Error' between the two images is the
	# sum of the squared difference between the two images;
	# NOTE: the two images must have the same dimension
	err = np.sum((imageA.astype("float") - imageB.astype("float")) ** 2)
	err /= float(imageA.shape[0] * imageA.shape[1])
	
	# return the MSE, the lower the error, the more "similar"
	# the two images are
	return err

if __name__ == "__main__":
	main()




