import random
import pygame

#font2 = pygame.font.SysFont("arialblack", 20)
#TEXT_COL = (76, 153, 0)

def draw_text(text, font, text_col, x, y):
	img = font.render(text, True, text_col)
	img_width = img.get_width()

def suma(nivel):

	if nivel == 1:
		x = random.randint(1, 9)
		y = random.randint(1, 9)

		suma = x + y
		return [x, y, suma, (suma + random.randint(1, 3)), (suma - random.randint(1, 3)), (suma + random.randint(1, 3))]

	if nivel == 2:
		x = random.randint(1, 9)
		y = random.randint(10, 99)

		suma = x + y
		return [x, y, suma, (suma + random.randint(1, 3)), (suma - random.randint(1, 3)), (suma + random.randint(1, 3))]

	if nivel == 3:
		x = random.randint(10, 99)
		y = random.randint(10, 99)

		suma = x + y
		return [x, y, suma, (suma + random.randint(1, 3)), (suma - random.randint(1, 3)), (suma + random.randint(1, 3))]

	print(f"{x}, {y}, {suma}")

def resta(nivel):

	if nivel == 1:
		x = random.randint(1, 9)
		y = random.randint(1, 9)

		if x >= y:
			resta = x - y
			return [x, y, resta, (resta + random.randint(1, 3)), (resta - random.randint(1, 3)), (resta + random.randint(1, 3))]
		else:
			resta = y - x
			return [x, y, resta, (resta + random.randint(1, 3)), (resta - random.randint(1, 3)), (resta + random.randint(1, 3))]

	if nivel == 2:
		x = random.randint(1, 9)
		y = random.randint(10, 99)

		if x >= y:
			resta = x - y
			return [x, y, resta, (resta + random.randint(1, 3)), (resta - random.randint(1, 3)), (resta + random.randint(1, 3))]
		else:
			resta = y - x
			return [x, y, resta, (resta + random.randint(1, 3)), (resta - random.randint(1, 3)), (resta + random.randint(1, 3))]

	if nivel == 3:
		x = random.randint(10, 99)
		y = random.randint(10, 99)

		if x >= y:
			resta = x - y
			return [x, y, resta, (resta + random.randint(1, 3)), (resta - random.randint(1, 3)), (resta + random.randint(1, 3))]
		else:
			resta = y - x
			return [x, y, resta, (resta + random.randint(1, 3)), (resta - random.randint(1, 3)), (resta + random.randint(1, 3))]



def multi(nivel):

	if nivel == 1:
		x = random.randint(1, 9)
		y = random.randint(1, 9)

		mult = x * y
		return [x, y, mult, (mult + random.randint(1, 3)), (mult - random.randint(1, 3)), (mult + random.randint(1, 3))]

	if nivel == 2:
		x = random.randint(1, 9)
		y = random.randint(10, 99)

		mult = x * y
		return [x, y, mult, (mult + random.randint(1, 3)), (mult - random.randint(1, 3)), (mult + random.randint(1, 3))]

	if nivel == 3:
		x = random.randint(10, 99)
		y = random.randint(10, 99)

		mult = x * y
		return [x, y, mult, (mult + random.randint(1, 3)), (mult - random.randint(1, 3)), (mult + random.randint(1, 3))]


def divi(nivel):

	if nivel == 1:
		x = random.randint(1, 9)
		y = random.randint(1, 9)
		if x >= y:
			div = round((x / y), 2)
			return [x, y, div, (div + random.randint(1, 3)), (div - random.randint(1, 3)), (div + random.randint(1, 3))]
		else:
			div = round((y / x), 2)
			return [y, x, div, (div + random.randint(1, 3)), (div - random.randint(1, 3)), (div + random.randint(1, 3))]

	if nivel == 2:
		x = random.randint(1, 9)
		y = random.randint(10, 99)

		if x >= y:
			div = round((x / y), 2)
			return [x, y, div, (div + random.randint(1, 3)), (div - random.randint(1, 3)), (div + random.randint(1, 3))]
		else:
			div = round((y / x), 2)
			return [y, x, div, (div + random.randint(1, 3)), (div - random.randint(1, 3)), (div + random.randint(1, 3))]

	if nivel == 3:
		x = random.randint(10, 99)
		y = random.randint(10, 99)

		if x >= y:
			div = round((x / y), 2)
			return [x, y, div, round((div + random.randint(1, 3)), 2), round((div - random.randint(1, 3)), 2), round((div + random.randint(1, 3)), 2)]
		else:
			div = round((y / x), 2)
			return [y, x, div, round((div + random.randint(1, 3)), 2), round((div - random.randint(1, 3)), 2), round((div + random.randint(1, 3)), 2)]
