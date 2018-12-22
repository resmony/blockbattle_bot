class Point(object):
	def __init__(self, x=None, y=None):
		if x is None and y is None:
			self.X = 0
			self.Y = 0
		else:
			self.X = x
			self.Y = y

	def set_location(self, x, y):
		self.X = x
		self.Y = y


if __name__ == '__main__':
	p = Point(2, 3)
