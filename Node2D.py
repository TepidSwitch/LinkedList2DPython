# Stanislav Schaller
# March 7th, 2016
# 2D Node 

class Node2D:
	'''Basic 2D Node'''

	def __init__(self, details = None, north = None, east = None, south = None, west = None):
		self.data = details
		self.north = north
		self.east = east
		self.south = south
		self.west = west

	def setData(self, details):
		'''Set the data slot'''
		self.data = details

	def getData(self):
		'''Get the stuff in the data slot'''
		return self.data

	def setNorth(self, north):
		'''Set the node to North'''
		self.north = north

	def getNorth(self):
		'''Return the node to the North, or None if at a border'''
		return self.north

	def setEast(self, east):
		'''Set the node to East'''
		self.east = east

	def getEast(self):
		'''Return the node to the East, or None if at a border'''
		return self.east

	def setSouth(self, south):
		'''Set the node to South'''
		self.south = south

	def getSouth(self):
		'''Return the node to the South, or None if at a border'''
		return self.south

	def setWest(self, west):
		'''Set the node to West'''
		self.west = west

	def getWest(self):
		'''Return the node to the West, or None if at a border'''
		return self.west

	def __str__(self):
		return str(self.data)