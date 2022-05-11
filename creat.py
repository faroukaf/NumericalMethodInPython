import math


def round(num):
	temp = num * 10 ** 5
	temp = int(temp)
	temp = int(str(temp)[-1])
	if temp < 5:
		return temp

def creat(fun, h, xs):
	print("i    |x    |  f(x)   |   2f(x)   |   4f(x)  ")
	i = 0
	n = xs.__len__()
	sumt = sumse = sumso = sumo = 0
	while i < n:
		temp = fun(xs[i])
		temp2 = 2 * temp
		temp4 = 2 * temp2
		print(f"{i}    {xs[i]}    |{temp}|{temp2}|{temp4}")
		if i !=0 and i != n - 1:
			sumt += temp2
			if i % 2 == 0:
				sumse += temp2
			else:
				sumso += temp4
		else:
			sumo += temp
		i += 1
	t = (h / 2) * (sumo + sumt)
	s = (h / 3) * (sumo + sumso + sumse)
	print(f"Trapezoidal: {t}\nSimpson's: {s}")


if __name__ == '__main__':
	fun = lambda x: math.pow(math.e, x) / math.sqrt(1 - x)
	fun2 = lambda x:math.sqrt(1 + x)
	h = 0.1
	x0 = 0.1
	xn = 1
	im = [0, .1, .2, .3, .4, .5, .6, .7, .8, .9]
	im2 = [0, .1, .2, .3, .4, .5]
	im3 = [0]
	i = 0
	while i < math.pi / 2:
		i += .1
		im3.append(i)
	creat(fun, h, im)

