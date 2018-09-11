#https://stackoverflow.com/questions/434583/what-is-the-fastest-way-to-draw-an-image-from-discrete-pixel-values-in-python
#  getting a feel for how to draw images in python
#https://www.hackerearth.com/practice/notes/extracting-pixel-values-of-an-image-in-python/
#  extracting pixel values from an image file
"""
Authors: Dustin Hines
Course: CS3725
Assignment: M2
Date: 9/12/2018
Description:  
	This module implements a markov chain to generate images based on a given training set.
	Currently, the training set is composed of a single image, but this could easily be expanded
	by reading in additional images.  From the training set, the likelihood of transitioning from a
	pixel of each color to the next is determined and put into a transition matrix.  To keep things 
	simpler and to avoid working with a 16777216x16777216 transition matrix, RGB pixel values are 
	simplified and broken into 64 distint values depending on the original R, G, and B values
	divided with integer division by 64 (Thus turning each color value in the pixel into one of 4
	values in the range [0,3]).  

	After calculating the transition matrix, 

Let it be known that I named everything using camel case until I read the style guide and needed
to then change all the variable, function names, etc.  ¯\_(ツ)_/¯  Thankfully, find and replace exists.
"""

import numpy 
import scipy.misc as scipy_misc
from PIL import Image as image_module
import random
import os

X_DIMENSION_GENERATED = 100
Y_DIMENSION_GENERATED = 100
RESIZE_X = 200
RESIZE_Y = 200
FINAL_X = 5000
FINAL_Y = 5000
WIDTH_COLOR_RANGES = 16
FILE_PATH = "input3"

def simple_colors(pixel):
	"""
	Purpose: Categorize the 256*256*256 possible colors normally available to a pixel
			 into 64 simple colors so that our transition matrix isnt 16777216x16777216
			 in size.
	Input: A pixel value given as a list of the R, G, and B values.
	Return: A list of pixel values where R, G, and B can each be a value in the range
		    [0,3], meaning that there 64 possible simple colors
	"""
	simplified = [pixel[0]//WIDTH_COLOR_RANGES, pixel[1]//WIDTH_COLOR_RANGES, pixel[2]//WIDTH_COLOR_RANGES]
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
	

def import_and_resize(image_path):
	"""
	Purpose: Helper function that imports an image from a given image path (specified by global)
			 and resizes and returns the images represented as a list of pixel values where 
			 each pixel is represented by a list of the R, G, and B color values.
	Input: Image path as a string.
	Return: List of pixel values for the resized images.
	"""
	training_set = []
	
	for file in os.listdir(FILE_PATH):
		if file[0] == '.':
			continue
		print(file)
		image = image_module.open(FILE_PATH + "/" + file)
		#image.show()
		#RESIZE_X/Y are specified with a global
		resized = image.resize((RESIZE_X, RESIZE_Y), image_module.BICUBIC)
		training_set.append(resized)
	"""
	image = image_module.open("input/download.jpeg")
	resized = image.resize((RESIZE_X, RESIZE_Y), image_module.BICUBIC)
	training_set.append(resized)
	"""
	return training_set


def translate_to_num(pixel):
	colors_in_range = 256 // WIDTH_COLOR_RANGES
	return pixel[0] * colors_in_range * colors_in_range + pixel[1] * colors_in_range + pixel[2] 


def translate_to_pixel(color_as_num):
	colors_in_range = 256 // WIDTH_COLOR_RANGES
	red = color_as_num // (colors_in_range * colors_in_range) % colors_in_range
	green = color_as_num // colors_in_range % colors_in_range
	blue = color_as_num % colors_in_range
	return [red, green, blue]


def calculate_transition_matrix(training_set):
	"""
	Purpose: 
	"""	
	transition_matrixes = []
	for image in training_set:
		transition_counts = []
		#create a zero filled 64x64 matrix as a list of lists
		num_colors = pow(256 // WIDTH_COLOR_RANGES, 3)
		for each in range(0, num_colors):
			row = [0] * num_colors
			transition_counts.append(row)
		for index in range(0,len(image) - 1):
			color_first = simple_colors(image[index])
			color_first_as_num = translate_to_num(color_first)
			next_pixel = image[index + 1]
			color_next = simple_colors(next_pixel)
			color_next_as_num = translate_to_num(color_next)
			transition_counts[color_first_as_num][color_next_as_num] += 1

		transition_matrix = transition_counts.copy()
		for row in range(0, len(transition_matrix)):
			row_sum = 0
			for value in transition_matrix[row]:
				row_sum += value
			if row_sum == 0:
				continue
			#for each value in the row, divide by sum for row overall 
			for column in range(0, len(transition_matrix[row])):
				transition_sum = transition_matrix[row][column] 
				transition_matrix[row][column] = transition_sum / row_sum
		#testing
		"""for row in transition_matrix:
			row_sum = 0
			for value in row:
				row_sum += value
			if row_sum != 0:
				print(row_sum)
			"""
		print("Finished transition matrix.")
		transition_matrixes.append(transition_matrix)
	print("All matrixes calculated.")
	return transition_matrixes


def main():

	training_set = import_and_resize(FILE_PATH)
	training_pixels = []
	for image in training_set:
		training_pixels.append(list(image.getdata()))
	starting_pixels = []
	for image in training_pixels:
		starting_pixels.append(simple_colors(image[0]))

	transition_matrixes = calculate_transition_matrix(training_pixels)
	generated_image = numpy.zeros((X_DIMENSION_GENERATED, Y_DIMENSION_GENERATED, 3), dtype=numpy.uint8)

	print(starting_pixels)
	state = translate_to_num(starting_pixels[0])
	print(state)
	num_matrixes = len(transition_matrixes)
	switch_matrix_per_rows = random.randint(X_DIMENSION_GENERATED//100, X_DIMENSION_GENERATED//10)
	curr_matrix = 0
	for row in range(0, len(generated_image)):
		print("Generated Image Row: {}".format(row + 1))
		if row == switch_matrix_per_rows:
			curr_matrix += 1
			curr_matrix = curr_matrix % num_matrixes
			switch_matrix_per_rows = switch_matrix_per_rows + random.randint(X_DIMENSION_GENERATED//100, X_DIMENSION_GENERATED//10)
			state = translate_to_num(starting_pixels[curr_matrix])
			

		for pixel in range(0, len(generated_image[row])):
			random_val = random.random()
			lower_end = 0
			trans_from_curr_state = transition_matrixes[curr_matrix][state]
			for index in range(0, len(trans_from_curr_state)):
				probability = trans_from_curr_state[index]

				if random_val < probability + lower_end:
					simple_next_pixel = translate_to_pixel(index)
					"""
					#some random numbers to expand the simplified pixels back throughout the ranges
					r1 = random.randint(0, 31)
					r2 = random.randint(0, 31)
					r3 = random.randint(0, 31)
					"""
					red_full_color = simple_next_pixel[0] * WIDTH_COLOR_RANGES 
					green_full_color = simple_next_pixel[1] * WIDTH_COLOR_RANGES 
					blue_full_color = simple_next_pixel[2] * WIDTH_COLOR_RANGES 
					generated_image[row][pixel] = [red_full_color, green_full_color, blue_full_color]
					state = index
					break
				lower_end += probability






	image = scipy_misc.toimage(generated_image)
	image.resize((FINAL_X, FINAL_Y), image_module.NEAREST)
	scipy_misc.imsave("curr_test.png", image)    
	image.show()                      			
	
main()