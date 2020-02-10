from random import randint
import sys
import defs
import pygame
import time

class Game:

	def generate(self):
		"""Generate an array representing a 16x16 grid with 40 mines."""

		self.grid = []
		for i in range(16):
			self.grid.append([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])

		for i in range(40):
			valid = False
			while not valid:
				xcord, ycord = randint(0, 15), randint(0, 15)
				if self.grid[xcord][ycord] != '*':
					self.grid[xcord][ycord] = '*'
					valid = True

		for xcord in range(15):
			for ycord in range(15):
				if self.grid[xcord][ycord] != '*':
					self.grid[xcord][ycord] = defs.get_value(self.grid, (xcord, ycord))


	def play(self):
		"""Initialize a game sequence and generate an array of known cells."""
		pygame.init()
		game_over = False

		screen = pygame.display.set_mode((450, 450))

		known = []
		for i in range(16):
			known.append([None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None])

		while True:
			pygame.time.delay(10)
			screen.fill((200, 200, 200))

			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					sys.exit()
				if event.type == pygame.MOUSEBUTTONDOWN:
					LEFT = 1
					RIGHT = 3
					pressed = defs.get_clicked()
					x = pressed[0]
					y = pressed[1]
					if not game_over:
						if event.button == LEFT and known[x][y] is None:
							known[x][y] = self.grid[x][y]
							if known[x][y] == '*':
								defs.draw_grid(known, screen)
								pygame.display.update()
								defs.playsound('explosion.wav')
								game_over = True
								time.sleep(1)
								self.generate()
								self.play()
								break
						if event.button == RIGHT:
							if known[x][y] is None:
								known[x][y] = 'X'
							elif known[x][y] == 'X':
								known[x][y] = None

			defs.reveal_zeros(known, self.grid)

			defs.draw_grid(known, screen)

			
			pygame.display.update()



a = Game()

a.generate()
a.play()
