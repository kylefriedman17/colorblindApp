# problems so far:
	# images need to have the same resolution
	# images with different color channels won't work#

from PIL import Image
from SSIM_PIL import compare_ssim

# the two images go here
img1 = Image.open(path)
img2 = Image.open(path)


# compares images and returns percent difference

def compare_images(imageA, imageB):
	compare = compare_ssim(img1, img2)
	compare += 1
	compare = 2 - compare
	compare /= 2
	return compare * 100


print(str(compare_images(img1, img2)) + "% difference")


