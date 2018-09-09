"""This is clearly a dumb was of accomplishing a mapping between vectors and a number
to represent them, but I was doing this when I was staying up for a sleep-deprived EEG 
and I thought it was pretty funny that I spent so much time doing it"""

def translateToNum(pixel):
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

def translateToPixel(colorAsNum):
	if colorAsNum == 0:
		return [0,0,0]
	elif colorAsNum == 1:
		return [0,0,1]
	elif colorAsNum == 2:
		return [0,0,2]
	elif colorAsNum == 3:
		return [0,0,3]
	elif colorAsNum == 4:
		return [0,1,0]
	elif colorAsNum == 5:
		return [0,1,1]
	elif colorAsNum == 6:
		return [0,1,2]
	elif colorAsNum == 7:
		return [0,1,3]
	elif colorAsNum == 8:
		return [0,2,0]
	elif colorAsNum == 9:
		return [0,2,1]
	elif colorAsNum == 10:
		return [0,2,2]
	elif colorAsNum == 11:
		return [0,2,3]
	elif colorAsNum == 12:
		return [0,3,0]
	elif colorAsNum == 13:
		return [0,3,1]
	elif colorAsNum == 14:
		return [0,3,2]
	elif colorAsNum == 15:
		return [0,3,3]

	elif colorAsNum == 16:
		return [1,0,0]
	elif colorAsNum == 17:
		return [1,0,1]
	elif colorAsNum == 18:
		return [1,0,2]
	elif colorAsNum == 19:
		return [1,0,3]
	elif colorAsNum == 20:
		return [1,1,0]
	elif colorAsNum == 21:
		return [1,1,1]
	elif colorAsNum == 22:
		return [1,1,2]
	elif colorAsNum == 23:
		return [1,1,3]
	elif colorAsNum == 24:
		return [1,2,0]
	elif colorAsNum == 25:
		return [1,2,1]
	elif colorAsNum == 26:
		return [1,2,2]
	elif colorAsNum == 27:
		return [1,2,3]
	elif colorAsNum == 28:
		return [1,3,0]
	elif colorAsNum == 29:
		return [1,3,1]
	elif colorAsNum == 30:
		return [1,3,2]
	elif colorAsNum == 31:
		return [1,3,3]

	elif colorAsNum == 32:
		return [2,0,0]
	elif colorAsNum == 33:
		return [2,0,1]
	elif colorAsNum == 34:
		return [2,0,2]
	elif colorAsNum == 35:
		return [2,0,3]
	elif colorAsNum == 36:
		return [2,1,0]
	elif colorAsNum == 37:
		return [2,1,1]
	elif colorAsNum == 38:
		return [2,1,2]
	elif colorAsNum == 39:
		return [2,1,3]
	elif colorAsNum == 40:
		return [2,2,0]
	elif colorAsNum == 41:
		return [2,2,1]
	elif colorAsNum == 42:
		return [2,2,2]
	elif colorAsNum == 43:
		return [2,2,3]
	elif colorAsNum == 44:
		return [2,3,0]
	elif colorAsNum == 45:
		return [2,3,1]
	elif colorAsNum == 46:
		return [2,3,2]
	elif colorAsNum == 47:
		return [2,3,3]

	elif colorAsNum == 48:
		return [3,0,0]
	elif colorAsNum == 49:
		return [3,0,1]
	elif colorAsNum == 50:
		return [3,0,2]
	elif colorAsNum == 51:
		return [3,0,3]
	elif colorAsNum == 52: 
		return [3,1,0]
	elif colorAsNum == 53:
		return [3,1,1]
	elif colorAsNum == 54:
		return [3,1,2]
	elif colorAsNum == 55:
		return [3,1,3]
	elif colorAsNum == 56:
		return [3,2,0]
	elif colorAsNum == 57:
		return [3,2,1]
	elif colorAsNum == 58:
		return [3,2,2]
	elif colorAsNum == 59:
		return [3,2,3]
	elif colorAsNum == 60:
		return [3,3,0]
	elif colorAsNum == 61:
		return [3,3,1]
	elif colorAsNum == 62:
		return [3,3,2]
	elif colorAsNum == 63:
		return [3,3,3]