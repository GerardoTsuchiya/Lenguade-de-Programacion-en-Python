import pygame

#Clase boton
class Button_Img():
	def __init__(self, x, y, image, scale):
		width = image.get_width()
		height = image.get_height()
		self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
		self.rect = self.image.get_rect()
		self.rect.topleft = (x, y)
		self.clicked = False

	def draw(self, surface, sound):

		accion = False

		#posicion del mouse
		pos = pygame.mouse.get_pos()

		#sobre y click
		if self.rect.collidepoint(pos):
			if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
				self.clicked = True
				accion = True
				sound.play()

		if pygame.mouse.get_pressed()[0] == 0:
			self.clicked = False

		#dibujar boton
		surface.blit(self.image, (self.rect.x, self.rect.y))

		return accion		