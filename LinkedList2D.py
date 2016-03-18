# Stanislav Schaller
# March 7th, 2016
# 2D Linked List Implementation

import Node2D

class LinkedList2D:
	'''A series of nodes holding data that point in four directions to either None (end of matrix) or another node'''

	first = None
	last = None
	work = None

	def __init__(self, matrix = None, length = 2, width = 2):
		if (matrix == None):
			# TODO: automate this process, decide on how 2D it's going to be
			self.first = Node2D.Node2D(None)
			self.first.setEast(Node2D.Node2D(None))
			self.first.setSouth(Node2D.Node2D(None))

			self.last = Node2D.Node2D(None)
			self.last.setNorth(self.first.getEast())
			self.last.setWest(self.first.getSouth())

			self.first.getEast().setSouth(self.last)
			self.first.getEast().setWest(self.first)

			self.first.getSouth().setEast(self.last)
			self.first.getSouth().setNorth(self.first)
		else:
			if (isinstance(matrix, list)):
				self.work = self.matrixBuild(matrix, length, width)
				print(self.work)
			else:
				print("Wrong type: please input a list")
				return None


	def matrixBuild(self, matrix, length, width):
		'''Private function that takes 1D array and makes it a 2D array representing a matrix based off of length and width.
		   Returns either a 2D array padded with Nones if the math wasn't even, or truncated if the area is smaller than the length of the list'''
		if ((length * width) < len(matrix)):
			out = self.crunch(matrix, length, width)
			helpful = matrix[length*width:]
			print("Truncated these from the input: " + str(helpful))
			return out
		elif ((length * width) > len(matrix)):
			over = length * width - len(matrix)
			while(len(matrix) != (length * width)):
				matrix.append(None)
			out = self.crunch(matrix, length, width)
			return out
		else:
			out = self.crunch(matrix, length, width)
			return out


	def crunch(self, matrix, length, width):
		output = []
		for i in range(0, length):
			sl = matrix[ width*i : width*(i+1) ]
			output.append(sl)
		return output

	def initLink(self, outMatrix):
		
		