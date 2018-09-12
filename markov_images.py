
"""
Authors: Dustin Hines
Course: CS3725
Assignment: M2
Date: 9/12/2018
Description:  
	This module implements a markov chain to generate images based on a given 
	training set.  Currently, the training set is composed of a single image,
	but this could easily be expanded by reading in additional images.  From 
	the training set, the likelihood of transitioning from a pixel of each 
	color to the next is determined and put into a transition matrix.  To keep
	things simpler and to avoid working with a 16777216x16777216 transition 
	matrix, RGB pixel values are simplified and broken into ranges smaller 
	than 256 as specified by WIDTH_COLOR_RANGES.  The range for each pixel 
	value becomes 256 divided by the WIDTH_COLOR_RANGES variable.   

	After calculating the transition matrix, 


Some things I looked at:
https://stackoverflow.com/questions/434583/what-is-the-fastest-way-to-draw-an-image-from-
	  discrete-pixel-values-in-python
->getting a feel for how to draw images in python
https://www.hackerearth.com/practice/notes/extracting-pixel-values-of-an-image-in-python/
->extracting pixel values from an image file

+scipy documentation on resizing

I also read a medium article (I think?) about Markov chains and images but I forget 
exactly what it was and I still have no idea how he was doing what he was doing since 
he was training on multiple images and producing an image that was a kind of strange blend
of them.  

*Let it be known that I named everything using camel case until I read the style guide and needed
to then change all the variable, function names, etc.  ¯\_(ツ)_/¯  Thankfully, find and replace exists.
"""

import numpy 
import scipy.misc as scipy_misc
from PIL import Image as image_module
import random
import os

X_DIM_GEN = 1000
Y_DIM_GEN = 100
RESIZE_X = 200
RESIZE_Y = 200
FINAL_X = 5000
FINAL_Y = 5000
WIDTH_COLOR_RANGES = 16
FILE_PATH = "input3"


def simple_colors(pixel):
	"""
	Purpose: Categorize the 256*256*256 possible colors normally available to a pixel
			 into (256//WIDTH_COLOR_RANGES)^3 simple colors so that our transition matrix 
			 isnt 16777216x16777216 in size (my computer doesnt have that much memory :( ).
	Input: A pixel value given as a list of the R, G, and B values.
	Return: A list of pixel values where R, G, and B can each be a value in the range
		    [0,256//16], meaning that there (256//16)^3 possible simple colors
	"""
	simple_red = pixel[0]//WIDTH_COLOR_RANGES
	simple_green = pixel[1]//WIDTH_COLOR_RANGES
	simple_blue = pixel[2]//WIDTH_COLOR_RANGES
	simplified = [simple_red, simple_green, simple_blue]
	return simplified


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
		#RESIZE_X/Y are specified with a global
		resized = image.resize((RESIZE_X, RESIZE_Y), image_module.BICUBIC)
		training_set.append(resized)

	return training_set


def translate_to_num(pixel):
	"""
	Purpose: Take a given pixel and associate it with a number unique to this pixel in the range
	[0, number of possible colors given the range simplification].  This is necessary to index
	into the transition_matrix with a color (can't index an array with a list as far as I know!)
	Input: A pixel represented by a list of 3 integer values.
	Return: A number in the range [0, number of possible colors].
	"""
	colors_in_range = 256 // WIDTH_COLOR_RANGES
	return pixel[0] * colors_in_range * colors_in_range + pixel[1] * colors_in_range + pixel[2] 


def translate_to_pixel(color_as_num):
	"""
	Purpose: Take a number representing a pixel (unique association) and turn it back 
	into a pixel.  
	Input: number in range[0, number of possible]
	Return: A pixel, represented as a list of the 3 color values, that is associated with the 
		    input number.  
	"""
	colors_in_range = 256 // WIDTH_COLOR_RANGES
	red = color_as_num // (colors_in_range * colors_in_range) % colors_in_range
	green = color_as_num // colors_in_range % colors_in_range
	blue = color_as_num % colors_in_range
	return [red, green, blue]


def calculate_transition_matrix(training_set):
	"""
	Purpose: Calculate a transition matrix for each image in the training set.
	Input: List of images where each image is represented by a list of pixels values 
		   where each pixel value is a list of the R, G, and B values.
	Return: A list of transition matrixes for each of the images in the input 
			training set.  
	"""	
	trans_matrixes = []
	for image in training_set:
		transition_counts = []
		#create a zero filled 64x64 matrix as a list of lists
		num_colors = pow(256 // WIDTH_COLOR_RANGES, 3)
		for each in range(0, num_colors):
			row = [0] * num_colors
			transition_counts.append(row)
		#for each pixel and the pixel after, count the transition
		for index in range(0,len(image) - 1):
			color_first = simple_colors(image[index])
			color_first_as_num = translate_to_num(color_first)
			next_pixel = image[index + 1]
			color_next = simple_colors(next_pixel)
			color_next_as_num = translate_to_num(color_next)
			transition_counts[color_first_as_num][color_next_as_num] += 1

		#turn the transition counts into a transition matrix 
		#	by summing the transitions per row and dividing 
		#	every item in this row sum 
		transition_matrix = transition_counts.copy()
		for row in range(0, len(transition_matrix)):
			row_sum = 0
			for value in transition_matrix[row]:
				row_sum += value
			if row_sum == 0:
				continue
			#for each value in the row, divide by sum of row overall 
			for column in range(0, len(transition_matrix[row])):
				transition_sum = transition_matrix[row][column] 
				transition_matrix[row][column] = transition_sum / row_sum
		
		print("Finished transition matrix.")
		trans_matrixes.append(transition_matrix)
	print("All matrixes calculated.")
	return trans_matrixes


def fill_gen_image(gen_image, trans_matrixes, start_pixels):
	"""
	Purpose: From a given transition matrix and array of pixels to use to generate
		images from each of the transition matrixes, fill a new images with pixels
		chosen randomly proportional to the transition probability determined by the 
		transition matrix.
	Input: The image to be filled with randomish pixels, the transition matrixes, 
		and an array of starting pixel values associated with each transition matrix.
	Return: The given 3D image array (X_DIM_GENxY_DIM_GENx3) populated with pixel values
	"""
	state = translate_to_num(start_pixels[0])
	num_matrixes = len(trans_matrixes)
	switch_matrix_per_rows = random.randint(X_DIM_GEN//100, X_DIM_GEN//10)
	curr_matrix = 0
	for row in range(0, len(gen_image)):
		print("Generated Image Row: {}".format(row + 1))
		if row == switch_matrix_per_rows:
			curr_matrix += 1
			curr_matrix = curr_matrix % num_matrixes
			rand_stripe_width = random.randint(X_DIM_GEN//100, X_DIM_GEN//10)
			switch_matrix_per_rows = switch_matrix_per_rows + rand_stripe_width
			state = translate_to_num(start_pixels[curr_matrix])
			

		for pixel in range(0, len(gen_image[row])):
			random_val = random.random()
			lower_end = 0
			trans_from_curr_state = trans_matrixes[curr_matrix][state]
			#imagine that the probability of chosing each transition is a slice of a pie
			#this finds the slice of the pie that our random number landed in
			for index in range(0, len(trans_from_curr_state)):
				probability = trans_from_curr_state[index]
				if random_val < probability + lower_end:
					#our random number is within this slice of the pie!
					simple_next_pixel = translate_to_pixel(index)
					#need to expand the pixel's color back into the color range 
					#	for a real pixel
					red_full_color = simple_next_pixel[0] * WIDTH_COLOR_RANGES 
					green_full_color = simple_next_pixel[1] * WIDTH_COLOR_RANGES 
					blue_full_color = simple_next_pixel[2] * WIDTH_COLOR_RANGES 
					next_pixel = [red_full_color, green_full_color, blue_full_color]
					gen_image[row][pixel] = next_pixel
					state = index
					break
				lower_end += probability
	return gen_image


def main():
	"""
	Purpose: main function that gets all the balls rolling. 
	Input: n/a
	Return: none
	"""
	training_set = import_and_resize(FILE_PATH)
	training_pixels = []
	#add image representation as pixels to a list 
	for image in training_set:
		training_pixels.append(list(image.getdata()))
	start_pixels = []
	for image in training_pixels:
		start_pixels.append(simple_colors(image[0]))

	trans_matrixes = calculate_transition_matrix(training_pixels)
	#the second stack overflow thread listed in the docstring is where this is from
	gen_image = numpy.zeros((X_DIM_GEN, Y_DIM_GEN, 3), dtype=numpy.uint8)
	gen_image = fill_gen_image(gen_image, trans_matrixes, start_pixels)
	#convert image back from pixel array to a real image format
	image = scipy_misc.toimage(gen_image)
	#resize so that the images are uniform regardless of X_GEN_DIM and Y_GEN_DIM
	image.resize((FINAL_X, FINAL_Y), image_module.NEAREST)
	scipy_misc.imsave("curr_test.png", image)    
	image.show()                      			
	
main()