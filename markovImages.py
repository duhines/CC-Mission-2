#https://stackoverflow.com/questions/434583/what-is-the-fastest-way-to-draw-an-image-from-discrete-pixel-values-in-python
#  getting a feel for how to draw images in python
#https://www.hackerearth.com/practice/notes/extracting-pixel-values-of-an-image-in-python/
#  extracting pixel values from an image file
"""
Authors: Dustin Hines
Course: CS3725
Assignment: M2

Let it be known that I named everything using camel case until I read the style guide and needed
to then change all the variable, function names, etc.  ¯\_(ツ)_/¯
"""

import numpy 
import scipy
from PIL import Image
import random
import importImage
import colorToNumber

X_DIMENSION_GENERATED = 50
Y_DIMENSION_GENERATED = 50
RESIZE_X = 50
RESIZE_Y = 50
FILE_PATH = '/Users/dhines/Desktop/picasso.png'

def simple_colors(pixel):
	"""
	Purpose: Categorize the 256*256*256 possible colors normally available to a pixel
			 into 64 simple colors so that our transition matrix isnt 16777216x16777216
			 in size.
	Input: A pixel value given as a list of the R, G, and B values.
	Return: A list of pixel values where R, G, and B can each be a value in the range
		    [0,3], meaning that there 64 possible simple colors
	"""
	simplified = [pixel[0]//64, pixel[1]//64, pixel[2]//64]
	return simplified




def determine_start(input_pixels):
	"""
	Purpose: Choose a starting pixel value based off the input image by adding up 
		     all the R, G, and B values and then using modulo division on all these
		     values to get them back in the range of a real pixel.
    Input: List of pixel values where each pixel value is a list of the R, G, and B
    	   Values.
   	Return: A list of the starting R, G, and B values.
   	"""
	red_sum = 0
	blue_sum = 0
	green_sum = 0

	for pixel in input_pixels:
		red_sum += pixel[0]
		green_sum += pixel[1]
		blue_sum += pixel[2]
		
	start = [red_sum % 255, green_sum % 255, blue_sum % 255]
	return start #start with a pixel of this color 
	

def import_and_resize(imagePath):
	image = Image.open(imagePath)
	resized = image.resize((resizeX, resizeY), Image.BICUBIC)
	return resized


def calculateTransitionMatrix(inputPixels):
	"""Possible Colors: 64
	"""

	transitionCounts = []
	for x in range(0,64):
		row = [0] * 64
		transitionCounts.append(row)

	for index in range(0,len(inputPixels) - 1):
		colorFirst = simpleColors(inputPixels[index])
		colorFirstAsNum = colorToNumber.translateToNum(colorFirst)
		nextPixel = inputPixels[index + 1]
		colorNext = simpleColors(nextPixel)
		colorNextAsNum = colorToNumber.translateToNum(colorNext)
		transitionCounts[colorFirstAsNum][colorNextAsNum] += 1

	transitionMatrix = transitionCounts
	for x in range(0, len(transitionMatrix)):
		rowSum = 0
		for value in transitionMatrix[x]:
			rowSum += value
		if rowSum == 0:
			continue
		for y in range(0, len(transitionMatrix[x])):
			transitionSum = transitionMatrix[x][y] 
			transitionMatrix[x][y] = transitionSum / rowSum

	for row in transitionMatrix:
		rowSum = 0
		for value in row:
			rowSum += value
		print(rowSum)
	return transitionMatrix


def main():

	image = importImage.importAndResize(filePath)
	inputPixelList = list(image.getdata())
	startingPixel = determineStart(inputPixelList)
	simpleStart = simpleColors(startingPixel)
	startAsNum = colorToNumber.translateToNum(simpleStart)
	transitionMatrix = calculateTransitionMatrix(inputPixelList)
	generatedImage = numpy.zeros((X_DIMENSION_GENERATED, Y_DIMENSION_GENERATED, 3), dtype=numpy.uint8)

	state = startAsNum
	for row in range(0, len(generatedImage)):
		for pixel in range(0, len(generatedImage[row])):
			randomVal = random.random()
			lowerEnd = 0
			transFromCurrState = transitionMatrix[state]
			for index in range(0, len(transFromCurrState)):
				probability = transFromCurrState[index]
				if probability + lowerEnd < randomVal:
					simpleNextPixel = colorToNumber.translateToPixel(index)
					#some random numbers to expand the simplified pixels back into real colors
					r1 = random.randint(0, 65)
					r2 = random.randint(0, 64)
					r3 = random.randint(0, 65)
					r4 = random.randint(0, 64)
					r5 = random.randint(0, 65)
					r6 = random.randint(0, 64)
					redFullColor = simpleNextPixel[0]*64 + r2
					greenFullColor = simpleNextPixel[1]*64 + r4
					blueFullColor = simpleNextPixel[2]*64 + r6
					generatedImage[row][pixel] = [redFullColor, greenFullColor, blueFullColor]
					#print(pixel)
					state = index
				lowerEnd += probability






	image = scipy.misc.toimage(generatedImage)       
	image.show()                      			
	
main()