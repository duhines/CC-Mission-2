"""This is clearly a dumb was of accomplishing a mapping between vectors and a number
to represent them, but I was doing this when I was staying up for a sleep-deprived EEG 
and I thought it was pretty funny that I spent so much time doing it"""
COLOR_RANGES = 8



	if pixel == [0,0,0]:
		return 0
	elif pixel == [0,0,1]:
		return 1
	elif pixel == [0,0,2]:
		return 2
	elif pixel == [0,0,3]:
		return 3
	elif pixel == [0,1,0]:
		return 4
	elif pixel == [0,1,1]:
		return 5
	elif pixel == [0,1,2]:
		return 6
	elif pixel == [0,1,3]:
		return 7
	elif pixel == [0,2,0]:
		return 8
	elif pixel == [0,2,1]:
		return 9
	elif pixel == [0,2,2]:
		return 10
	elif pixel == [0,2,3]:
		return 11
	elif pixel == [0,3,0]:
		return 12
	elif pixel == [0,3,1]:
		return 13
	elif pixel == [0,3,2]:
		return 14
	elif pixel == [0,3,3]:
		return 15

	elif pixel == [1,0,0]:
		return 16
	elif pixel == [1,0,1]:
		return 17
	elif pixel == [1,0,2]:
		return 18
	elif pixel == [1,0,3]:
		return 19
	elif pixel == [1,1,0]:
		return 20
	elif pixel == [1,1,1]:
		return 21
	elif pixel == [1,1,2]:
		return 22
	elif pixel == [1,1,3]:
		return 23
	elif pixel == [1,2,0]:
		return 24
	elif pixel == [1,2,1]:
		return 25
	elif pixel == [1,2,2]:
		return 26
	elif pixel == [1,2,3]:
		return 27
	elif pixel == [1,3,0]:
		return 28
	elif pixel == [1,3,1]:
		return 29
	elif pixel == [1,3,2]:
		return 30
	elif pixel == [1,3,3]:
		return 31

	elif pixel == [2,0,0]:
		return 32
	elif pixel == [2,0,1]:
		return 33
	elif pixel == [2,0,2]:
		return 34
	elif pixel == [2,0,3]:
		return 35
	elif pixel == [2,1,0]:
		return 36
	elif pixel == [2,1,1]:
		return 37
	elif pixel == [2,1,2]:
		return 38
	elif pixel == [2,1,3]:
		return 39
	elif pixel == [2,2,0]:
		return 40
	elif pixel == [2,2,1]:
		return 41
	elif pixel == [2,2,2]:
		return 42
	elif pixel == [2,2,3]:
		return 43
	elif pixel == [2,3,0]:
		return 44
	elif pixel == [2,3,1]:
		return 45
	elif pixel == [2,3,2]:
		return 46
	elif pixel == [2,3,3]:
		return 47

	elif pixel == [3,0,0]:
		return 48
	elif pixel == [3,0,1]:
		return 49
	elif pixel == [3,0,2]:
		return 50
	elif pixel == [3,0,3]:
		return 51
	elif pixel == [3,1,0]:
		return 52
	elif pixel == [3,1,1]:
		return 53
	elif pixel == [3,1,2]:
		return 54
	elif pixel == [3,1,3]:
		return 55
	elif pixel == [3,2,0]:
		return 56
	elif pixel == [3,2,1]:
		return 57
	elif pixel == [3,2,2]:
		return 58
	elif pixel == [3,2,3]:
		return 59
	elif pixel == [3,3,0]:
		return 60
	elif pixel == [3,3,1]:
		return 61
	elif pixel == [3,3,2]:
		return 62
	elif pixel == [3,3,3]:
		return 63

def translate_to_pixel(color_as_num):
	colors_in_range = 256 // COLOR_RANGES
	red = color_as_num // (colors_in_range * colors_in_range) % colors_in_range
	green = color_as_num // colors_in_range % colors_in_range
	blue = color_as_num % colors_in_range
	return [red, green, blue]
	if color_as_num == 0:
		return [0,0,0]
	elif color_as_num == 1:
		return [0,0,1]
	elif color_as_num == 2:
		return [0,0,2]
	elif color_as_num == 3:
		return [0,0,3]
	elif color_as_num == 4:
		return [0,1,0]
	elif color_as_num == 5:
		return [0,1,1]
	elif color_as_num == 6:
		return [0,1,2]
	elif color_as_num == 7:
		return [0,1,3]
	elif color_as_num == 8:
		return [0,2,0]
	elif color_as_num == 9:
		return [0,2,1]
	elif color_as_num == 10:
		return [0,2,2]
	elif color_as_num == 11:
		return [0,2,3]
	elif color_as_num == 12:
		return [0,3,0]
	elif color_as_num == 13:
		return [0,3,1]
	elif color_as_num == 14:
		return [0,3,2]
	elif color_as_num == 15:
		return [0,3,3]

	elif color_as_num == 16:
		return [1,0,0]
	elif color_as_num == 17:
		return [1,0,1]
	elif color_as_num == 18:
		return [1,0,2]
	elif color_as_num == 19:
		return [1,0,3]
	elif color_as_num == 20:
		return [1,1,0]
	elif color_as_num == 21:
		return [1,1,1]
	elif color_as_num == 22:
		return [1,1,2]
	elif color_as_num == 23:
		return [1,1,3]
	elif color_as_num == 24:
		return [1,2,0]
	elif color_as_num == 25:
		return [1,2,1]
	elif color_as_num == 26:
		return [1,2,2]
	elif color_as_num == 27:
		return [1,2,3]
	elif color_as_num == 28:
		return [1,3,0]
	elif color_as_num == 29:
		return [1,3,1]
	elif color_as_num == 30:
		return [1,3,2]
	elif color_as_num == 31:
		return [1,3,3]

	elif color_as_num == 32:
		return [2,0,0]
	elif color_as_num == 33:
		return [2,0,1]
	elif color_as_num == 34:
		return [2,0,2]
	elif color_as_num == 35:
		return [2,0,3]
	elif color_as_num == 36:
		return [2,1,0]
	elif color_as_num == 37:
		return [2,1,1]
	elif color_as_num == 38:
		return [2,1,2]
	elif color_as_num == 39:
		return [2,1,3]
	elif color_as_num == 40:
		return [2,2,0]
	elif color_as_num == 41:
		return [2,2,1]
	elif color_as_num == 42:
		return [2,2,2]
	elif color_as_num == 43:
		return [2,2,3]
	elif color_as_num == 44:
		return [2,3,0]
	elif color_as_num == 45:
		return [2,3,1]
	elif color_as_num == 46:
		return [2,3,2]
	elif color_as_num == 47:
		return [2,3,3]

	elif color_as_num == 48:
		return [3,0,0]
	elif color_as_num == 49:
		return [3,0,1]
	elif color_as_num == 50:
		return [3,0,2]
	elif color_as_num == 51:
		return [3,0,3]
	elif color_as_num == 52: 
		return [3,1,0]
	elif color_as_num == 53:
		return [3,1,1]
	elif color_as_num == 54:
		return [3,1,2]
	elif color_as_num == 55:
		return [3,1,3]
	elif color_as_num == 56:
		return [3,2,0]
	elif color_as_num == 57:
		return [3,2,1]
	elif color_as_num == 58:
		return [3,2,2]
	elif color_as_num == 59:
		return [3,2,3]
	elif color_as_num == 60:
		return [3,3,0]
	elif color_as_num == 61:
		return [3,3,1]
	elif color_as_num == 62:
		return [3,3,2]
	elif color_as_num == 63:
		return [3,3,3]