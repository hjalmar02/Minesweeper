import pygame
import copy


def get_value(grid: list, pos: tuple):
	"""Get number of adjecent mine for square in pos."""

	x, y = pos[0], pos[1]  # x- and y-coordinate

	value = 0

	if y > 0:
		if x > 0:
			if grid[x-1][y-1] == '*':
				value += 1
		if grid[x][y-1] == '*':
			value += 1
		if x < 15:
			if grid[x+1][y-1] == '*':
				value += 1

	if x > 0:
		if grid[x-1][y] == '*':
			value += 1
	if x < 15:
		if grid[x+1][y] == '*':
			value += 1

	if y < 15:
		if x > 0:
			if grid[x-1][y+1] == '*':
				value += 1
		if grid[x][y+1] == '*':
			value += 1
		if x < 15:
			if grid[x+1][y+1] == '*':
				value += 1

	return value


def load_image(filename: str):

	return pygame.image.load('assets/' + filename)


def draw_grid(grid, display):

	for x in range(15):
		for y in range(15):
			
			if grid[x][y] is not None:  # cell has been opened
				if grid[x][y] == 0:  # no adjecent mines
					display.blit(load_image('default.png'), (x * 30, y * 30))
				elif grid[x][y] == '*':
					display.blit(load_image('mine.png'), (x * 30, y * 30))
				elif grid[x][y] == 'X':
					display.blit(load_image('flag.png'), (x * 30, y * 30))
				else:
					display.blit(load_image(str(grid[x][y]) + '.png'), (x * 30, y * 30))
			else:  # cell has not been opened
				display.blit(load_image('unopened.png'), (x * 30, y * 30))



def get_clicked():

	pos = pygame.mouse.get_pos()

	xcord, ycord = pos[0], pos[1]

	pressed_cell = (int(xcord / 30), int(ycord / 30))

	return pressed_cell


def reveal_zeros(grid, solution):

	oldgrid = copy.deepcopy(grid)

	for x in range(16):
		for y in range(16):

			if grid[x][y] == 0:
				if y > 0:
					if x > 0:
						grid[x-1][y-1] = solution[x-1][y-1]
					grid[x][y-1] = solution[x][y-1]
					if x < 15:
						grid[x+1][y-1] = solution[x+1][y-1]

				if x > 0:
					grid[x-1][y] = solution[x-1][y]
				if x < 15:
					grid[x+1][y] = solution[x+1][y]

				if y < 15:
					if x > 0:
						grid[x-1][y+1] = solution[x-1][y+1]
					grid[x][y+1] = solution[x][y+1]
					if x < 15:
						grid[x+1][y+1] = solution[x+1][y+1]


def playsound(filename):
	pygame.mixer.Sound('assets/' + filename).play()
