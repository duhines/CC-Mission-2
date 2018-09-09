import numpy 
import scipy.misc 
from PIL import Image
import random

def importAndResize(imagePath):
	resizeX = 2000
	resizeY = 2000
	image = Image.open(imagePath)
	resized = image.resize((resizeX, resizeY), Image.BICUBIC)
	return resized