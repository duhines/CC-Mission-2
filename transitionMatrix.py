class transitionMatrix:
	def __init__(self, numColors, inputPixels):
		self.numColors = numColors
		self.inputPixels = inputPixels
		self.transitionMatrix = [numColors][numColors] * None
