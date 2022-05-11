import math


class Interpolation:
	"""
	help solve interpolation problem by:
	+ linear
	+ lagrnarge
	+ Newton:
		forward
		backward
		divided

	"""
	def __init__(self, xs, ys):
		"""
		xs, ys: the value of x-value and has opsite y-value
		dif: the difrent table
		difx: for 3th Newton's method
		"""
		try:
			flag = "len"
			if len(xs) != len(ys):
				raise ValueError("xs and ys should have the same length")
			flag = "x-value type"
			for i in xs:
				if type(i) != int or type(i) != float:
					raise TypeError
			flag = "y-value type"
			for i in ys:
				if type(i) != int or type(i) != float:
					raise TypeError
		except TypeError:
			if flag == "len":
				raise TypeError("xs and ys should have len attrbuite")
			elif flag == "x-value type":
				raise TypeError("all x-value should be float or int")
			else:
				raise TypeError("all y-value should be float or int")

		self.xs = xs
		self.ys = ys
		self.dif = []
		self.difx = []

	def find_lase_than_point(self, x):
		"""
		(number) -> int
		find first index lase
		"""

	def liner_interpolation(self, x):
		"""
		(int or float, int or float) -> float

		take x-value and give his corspinding y-value in linear interploatin way

		____________________
		|    X    |    Y   |
		@@@@@@@@@@@@@@@@@@@@
		|    3    |    4   |
		@@@@@@@@@@@@@@@@@@@@
		|    5    |    9   |
		@@@@@@@@@@@@@@@@@@@@
		|    7    |    6   |
		--------------------

		#>>> linerInterpolation(4)
		6.5
		#>>> linerInterpolation(6.5)
		6.75
		#>>> linerInterpolation(8)
		raise OutRangeError
		"""

		# check if type aand value fit the requremented issuse
		if type(x) != int or type(x) != float:
			raise TypeError("x should be number")
		if x > self.xs[1] or x < self.x[0]:
			raise Interpolation.OutRangeError(f"{x} out of range of xs value")

		# find bounders

		i = 0




	
class OutRangeError(Exception):
		"""
		raise if tring interploting out of range point
		"""