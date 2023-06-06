import pygame
import buttonimg
import buttontext
import funciones
import random
import time

pygame.init()

#musica del juego
bg_music = pygame.mixer.Sound('musica.mp3')
bg_music.play(loops = -1)
bg_music.set_volume(0.1)

#sonido de los botones
bnt_sound = pygame.mixer.Sound('boton.mp3')
btn_correct = pygame.mixer.Sound('correct.mp3')
btn_correct.set_volume(0.4)
btn_incorrect = pygame.mixer.Sound('incorrect.mp3')
btn_incorrect.set_volume(0.4)
btn_corasound = pygame.mixer.Sound('corazon.mp3')
btn_corasound.set_volume(0.4)

#Creando ventana
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 563

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Math Quiz')

#Variables del juego
menu_state = "main"

#Cargando imagenes
img_start = pygame.image.load('Imagenes/start_btn.png').convert_alpha()
img_exit = pygame.image.load('Imagenes/exit_btn.png').convert_alpha()
img_suma = pygame.image.load('Imagenes/sumas.png').convert_alpha()
img_resta = pygame.image.load('Imagenes/restas.png').convert_alpha()
img_multi = pygame.image.load('Imagenes/multi.png').convert_alpha()
img_div = pygame.image.load('Imagenes/div(1).png').convert_alpha()
img_volver = pygame.image.load('Imagenes/volver.png').convert_alpha()
img_lv1 = pygame.image.load('Imagenes/lv1.png').convert_alpha()
img_lv2 = pygame.image.load('Imagenes/lv2.png').convert_alpha()
img_lv3 = pygame.image.load('Imagenes/lv3.png').convert_alpha()
img_fondo = pygame.image.load('Imagenes/fondo.png').convert_alpha()
img_corazon = pygame.image.load('Imagenes/corazon.png').convert_alpha()

#instancias botones operacion
btn_suma = buttonimg.Button_Img(100, 175, img_suma, 0.8)
btn_resta = buttonimg.Button_Img(518, 175, img_resta, 0.8)
btn_multi = buttonimg.Button_Img(100, 425, img_multi, 0.8)
btn_divi = buttonimg.Button_Img(518, 425, img_div, 0.8)

#instancias botones nivel
btn_cora1 = buttonimg.Button_Img(650, 5, img_corazon, 2)
btn_cora2 = buttonimg.Button_Img(700, 5, img_corazon, 2)
btn_cora3 = buttonimg.Button_Img(750, 5, img_corazon, 2)
btn_lvl1 = buttonimg.Button_Img((SCREEN_WIDTH/2) - 110, 175, img_lv1, 0.8)
btn_lvl2 = buttonimg.Button_Img((SCREEN_WIDTH/2) - 110, 300, img_lv2, 0.8)
btn_lvl3 = buttonimg.Button_Img((SCREEN_WIDTH/2) - 110, 425, img_lv3, 0.8)
btn_return = buttonimg.Button_Img(0, 0, img_volver, 0.3)


#definiendo font
font = pygame.font.SysFont("arialblack", 40)
font2 = pygame.font.SysFont("arialblack", 30)

#definiendo color
TEXT_COL = (102, 0, 51)

def draw_text(text, font, text_col, x, y):
	img = font.render(text, True, text_col)
	img_width = img.get_width()

	screen.blit(img, ((SCREEN_WIDTH/2)-(img_width/2), y))

#game loop
run = True
while run:

	screen.fill((202, 228, 241))
	screen.blit(img_fondo,(0,0))

#menu principal
	if menu_state == "main":
		#draw menu principal
		draw_text("Bienvenido a Math Quiz!", font, TEXT_COL, 400, 50)
		if btn_suma.draw(screen, bnt_sound) and clicked == False:
			print("Suma")
			menu_state = "niveles_suma"
			clicked = True
		if btn_resta.draw(screen, bnt_sound) and clicked == False:
			print("Resta")
			menu_state = "niveles_resta"
			clicked = True
		if btn_multi.draw(screen, bnt_sound) and clicked == False:
			print("Multi")
			menu_state = "niveles_multi"
			clicked = True
		if btn_divi.draw(screen, bnt_sound) and clicked == False:
			print("Divi")
			menu_state = "niveles_divi"
			clicked = True

		vidas = 3
		clicked = False
		val_suma1 = funciones.suma(1)
		val_suma2 = funciones.suma(2)
		val_suma3 = funciones.suma(3)
		val_resta1 = funciones.resta(1)
		val_resta2 = funciones.resta(2)
		val_resta3 = funciones.resta(3)
		val_multi1 = funciones.multi(1)
		val_multi2 = funciones.multi(2)
		val_multi3 = funciones.multi(3)
		val_divi1 = funciones.divi(1)
		val_divi2 = funciones.divi(2)
		val_divi3 = funciones.divi(3)

		num = list(range(2, 6))
		lista = random.sample(num, 4)


#eleccion de niveles
	elif menu_state == "niveles_suma":
		draw_text("Escoge tu nivel!", font, TEXT_COL, 145, 50)
		if btn_lvl1.draw(screen, bnt_sound) and clicked == False:
			print("Nivel_suma1")
			menu_state = "suma1"
			clicked = True

		if btn_lvl2.draw(screen, bnt_sound) and clicked == False:
			print("Nivel_suma2")
			menu_state = "suma2"
			clicked = True

		if btn_lvl3.draw(screen, bnt_sound) and clicked == False:
			print("Nivel_suma3")
			menu_state = "suma3"
			clicked = True

		if btn_return.draw(screen, bnt_sound):
			menu_state = "main"

	elif menu_state == "niveles_resta":
		draw_text("Escoge tu nivel!", font, TEXT_COL, 145, 50)
		if btn_lvl1.draw(screen, bnt_sound) and clicked == False:
			print("Nivel_resta1")
			menu_state = "resta1"
			clicked = True

		if btn_lvl2.draw(screen, bnt_sound) and clicked == False:
			print("Nivel_resta2")
			menu_state = "resta2"
			clicked = True

		if btn_lvl3.draw(screen, bnt_sound) and clicked == False:
			print("Nivel_resta3")
			menu_state = "resta3"
			clicked = True
		if btn_return.draw(screen, bnt_sound):
			menu_state = "main"

	elif menu_state == "niveles_multi":
		draw_text("Escoge tu nivel!", font, TEXT_COL, 145, 50)
		if btn_lvl1.draw(screen, bnt_sound) and clicked == False:
			print("Nivel_multi1")
			menu_state = "multi1"
			clicked = True

		if btn_lvl2.draw(screen, bnt_sound) and clicked == False:
			print("Nivel_multi2")
			menu_state = "multi2"
			clicked = True

		if btn_lvl3.draw(screen, bnt_sound) and clicked == False:
			print("Nivel_multi3")
			menu_state = "multi3"
			clicked = False
		if btn_return.draw(screen, bnt_sound):
			menu_state = "main"

	elif menu_state == "niveles_divi":
		draw_text("Escoge tu nivel!", font, TEXT_COL, 145, 50)
		if btn_lvl1.draw(screen, bnt_sound) and clicked == False:
			print("Nivel_divi1")
			menu_state = "divi1"
			clicked = True

		if btn_lvl2.draw(screen, bnt_sound) and clicked == False:
			print("Nivel_divi2")
			menu_state = "divi2"
			clicked = True

		if btn_lvl3.draw(screen, bnt_sound) and clicked == False:
			print("Nivel_divi3")
			menu_state = "divi3"
			clicked = True
		if btn_return.draw(screen, bnt_sound):
			menu_state = "main"

#nivel 1 suma
	elif menu_state == "suma1":
		if vidas == 3:
			btn_cora1.draw(screen, btn_corasound)
			btn_cora2.draw(screen, btn_corasound)
			btn_cora3.draw(screen, btn_corasound)
		elif vidas == 2:
			btn_cora3.draw(screen, btn_corasound)
			btn_cora2.draw(screen, btn_corasound)
		elif vidas == 1:
			btn_cora3.draw(screen, btn_corasound)
		elif vidas == 0:
			menu_state = "main"	

		btn1 = buttontext.Button_Text(150, 200, f"{val_suma1[lista[0]]}")
		btn2 = buttontext.Button_Text(450, 200, f"{val_suma1[lista[1]]}")
		btn3 = buttontext.Button_Text(150, 350, f"{val_suma1[lista[2]]}")
		btn4 = buttontext.Button_Text(450, 350, f"{val_suma1[lista[3]]}")

		draw_text("¿Cual es el resultado de esta suma?", font2, TEXT_COL, 145, 50)
		draw_text(f"{val_suma1[0]} + {val_suma1[1]}", font2, TEXT_COL, 250, 100)
		if btn1.drawtxt(screen) and clicked == False:
			if val_suma1[lista[0]] == val_suma1[2]:
				btn_correct.play()
				time.sleep(0.15)
			else:
				btn_incorrect.play()
				vidas = vidas - 1
			clicked = True
			random.shuffle(lista)
			val_suma1 = funciones.suma(1)

		if btn2.drawtxt(screen) and clicked == False:
			if val_suma1[lista[1]] == val_suma1[2]:
				btn_correct.play()
				time.sleep(0.15)
			else:
				btn_incorrect.play()
				vidas = vidas - 1
			clicked = True
			random.shuffle(lista)
			val_suma1 = funciones.suma(1)

		if btn3.drawtxt(screen) and clicked == False:
			if val_suma1[lista[2]] == val_suma1[2]:
				btn_correct.play()
				time.sleep(0.15)
			else:
				btn_incorrect.play()
				vidas = vidas - 1
			clicked = True
			random.shuffle(lista)
			val_suma1 = funciones.suma(1)

		if btn4.drawtxt(screen) and clicked == False:
			if val_suma1[lista[3]] == val_suma1[2]:
				btn_correct.play()
				time.sleep(0.15)
			else:
				btn_incorrect.play()
				vidas = vidas - 1
			clicked = True
			random.shuffle(lista)
			val_suma1 = funciones.suma(1)

		if btn_return.draw(screen, bnt_sound):
			random.shuffle(lista)
			val_suma1 = funciones.suma(1)
			menu_state = "niveles_suma"
   
#nivel 2 suma
	elif menu_state == "suma2":
		if vidas == 3:
			btn_cora1.draw(screen, btn_corasound)
			btn_cora2.draw(screen, btn_corasound)
			btn_cora3.draw(screen, btn_corasound)
		elif vidas == 2:
			btn_cora3.draw(screen, btn_corasound)
			btn_cora2.draw(screen, btn_corasound)
		elif vidas == 1:
			btn_cora3.draw(screen, btn_corasound)
		elif vidas == 0:
			menu_state = "main"	

		btn1 = buttontext.Button_Text(150, 200, f"{val_suma2[lista[0]]}")
		btn2 = buttontext.Button_Text(450, 200, f"{val_suma2[lista[1]]}")
		btn3 = buttontext.Button_Text(150, 350, f"{val_suma2[lista[2]]}")
		btn4 = buttontext.Button_Text(450, 350, f"{val_suma2[lista[3]]}")

		draw_text("¿Cual es el resultado de esta suma?", font2, TEXT_COL, 145, 50)
		draw_text(f"{val_suma2[0]} + {val_suma2[1]}", font2, TEXT_COL, 250, 100)
		if btn1.drawtxt(screen) and clicked == False:
			if val_suma2[lista[0]] == val_suma2[2]:
				btn_correct.play()
				time.sleep(0.15)
			else:
				btn_incorrect.play()
				vidas = vidas - 1

			clicked = True
			random.shuffle(lista)
			val_suma2 = funciones.suma(2)

		if btn2.drawtxt(screen) and clicked == False:
			if val_suma2[lista[1]] == val_suma2[2]:
				btn_correct.play()
				time.sleep(0.15)
			else:
				btn_incorrect.play()
				vidas = vidas - 1

			clicked = True
			random.shuffle(lista)
			val_suma2 = funciones.suma(2)

		if btn3.drawtxt(screen) and clicked == False:
			if val_suma2[lista[2]] == val_suma2[2]:
				
				btn_correct.play()
				time.sleep(0.15)
			else:
				btn_incorrect.play()
				vidas = vidas - 1
			clicked = True
			random.shuffle(lista)
			val_suma2 = funciones.suma(2)

		if btn4.drawtxt(screen) and clicked == False:
			if val_suma2[lista[3]] == val_suma2[2]:
				btn_correct.play()
				time.sleep(0.15)
			else:
				btn_incorrect.play()
				vidas = vidas - 1
			clicked = True
			random.shuffle(lista)
			val_suma2 = funciones.suma(2)
		if btn_return.draw(screen, bnt_sound):
			random.shuffle(lista)
			val_suma2 = funciones.suma(2)
			menu_state = "niveles_suma"
   
#nivel 3 suma
	elif menu_state == "suma3":
		if vidas == 3:
			btn_cora1.draw(screen, btn_corasound)
			btn_cora2.draw(screen, btn_corasound)
			btn_cora3.draw(screen, btn_corasound)
		elif vidas == 2:
			btn_cora3.draw(screen, btn_corasound)
			btn_cora2.draw(screen, btn_corasound)
		elif vidas == 1:
			btn_cora3.draw(screen, btn_corasound)
		elif vidas == 0:
			menu_state = "main"	

		btn1 = buttontext.Button_Text(150, 200, f"{val_suma3[lista[0]]}")
		btn2 = buttontext.Button_Text(450, 200, f"{val_suma3[lista[1]]}")
		btn3 = buttontext.Button_Text(150, 350, f"{val_suma3[lista[2]]}")
		btn4 = buttontext.Button_Text(450, 350, f"{val_suma3[lista[3]]}")

		draw_text("¿Cual es el resultado de esta suma?", font2, TEXT_COL, 145, 50)
		draw_text(f"{val_suma3[0]} + {val_suma3[1]}", font2, TEXT_COL, 250, 100)
		if btn1.drawtxt(screen) and clicked == False:
			if val_suma3[lista[0]] == val_suma3[2]:
				btn_correct.play()
				time.sleep(0.15)
			else:
				btn_incorrect.play()
				vidas = vidas - 1
			clicked = True
			random.shuffle(lista)
			val_suma3 = funciones.suma(3)

		if btn2.drawtxt(screen) and clicked == False:
			if val_suma3[lista[1]] == val_suma3[2]:
				btn_correct.play()
				time.sleep(0.15)
			else:
				btn_incorrect.play()
				vidas = vidas - 1
			clicked = True
			random.shuffle(lista)
			val_suma3 = funciones.suma(3)

		if btn3.drawtxt(screen) and clicked == False:
			if val_suma3[lista[2]] == val_suma3[2]:
				btn_correct.play()
				time.sleep(0.15)
			else:
				btn_incorrect.play()
				vidas = vidas - 1
			clicked = True
			random.shuffle(lista)
			val_suma3 = funciones.suma(3)

		if btn4.drawtxt(screen) and clicked == False:
			if val_suma3[lista[3]] == val_suma3[2]:
				btn_correct.play()
				time.sleep(0.15)
			else:
				btn_incorrect.play()
				vidas = vidas - 1
			clicked = True
			random.shuffle(lista)
			val_suma3 = funciones.suma(3)
		if btn_return.draw(screen, bnt_sound):
			random.shuffle(lista)
			val_suma3 = funciones.suma(3)
			menu_state = "niveles_suma"

#nivel 1 resta
	elif menu_state == "resta1":
		if vidas == 3:
			btn_cora1.draw(screen, btn_corasound)
			btn_cora2.draw(screen, btn_corasound)
			btn_cora3.draw(screen, btn_corasound)
		elif vidas == 2:
			btn_cora3.draw(screen, btn_corasound)
			btn_cora2.draw(screen, btn_corasound)
		elif vidas == 1:
			btn_cora3.draw(screen, btn_corasound)
		elif vidas == 0:
			menu_state = "main"	

		btn1 = buttontext.Button_Text(150, 200, f"{val_resta1[lista[0]]}")
		btn2 = buttontext.Button_Text(450, 200, f"{val_resta1[lista[1]]}")
		btn3 = buttontext.Button_Text(150, 350, f"{val_resta1[lista[2]]}")
		btn4 = buttontext.Button_Text(450, 350, f"{val_resta1[lista[3]]}")

		draw_text("¿Cual es el resultado de esta resta?", font2, TEXT_COL, 145, 50)
		if val_resta1[0] > val_resta1[1]:
			draw_text(f"{val_resta1[0]} - {val_resta1[1]}", font2, TEXT_COL, 250, 100)
		else:
			draw_text(f"{val_resta1[1]} - {val_resta1[0]}", font2, TEXT_COL, 250, 100)

		if btn1.drawtxt(screen) and clicked == False:
			if val_resta1[lista[0]] == val_resta1[2]:
				btn_correct.play()
				time.sleep(0.15)
			else:
				btn_incorrect.play()
				vidas = vidas - 1
			clicked = True
			random.shuffle(lista)
			val_resta1 = funciones.resta(1)

		if btn2.drawtxt(screen) and clicked == False:
			if val_resta1[lista[1]] == val_resta1[2]:
				btn_correct.play()
				time.sleep(0.15)
			else:
				btn_incorrect.play()
				vidas = vidas - 1
			clicked = True
			random.shuffle(lista)
			val_resta1 = funciones.resta(1)

		if btn3.drawtxt(screen) and clicked == False:
			if val_resta1[lista[2]] == val_resta1[2]:
				btn_correct.play()
				time.sleep(0.15)
			else:
				btn_incorrect.play()
				vidas = vidas - 1
			clicked = True
			random.shuffle(lista)
			val_resta1 = funciones.resta(1)

		if btn4.drawtxt(screen) and clicked == False:
			if val_resta1[lista[3]] == val_resta1[2]:
				btn_correct.play()
				time.sleep(0.15)
			else:
				btn_incorrect.play()
				vidas = vidas - 1
			clicked = True
			random.shuffle(lista)
			val_resta1 = funciones.resta(1)

		if btn_return.draw(screen, bnt_sound):
			random.shuffle(lista)
			val_resta1 = funciones.resta(1)
			menu_state = "niveles_resta"

#nivel 2 resta
	elif menu_state == "resta2":
		if vidas == 3:
			btn_cora1.draw(screen, btn_corasound)
			btn_cora2.draw(screen, btn_corasound)
			btn_cora3.draw(screen, btn_corasound)
		elif vidas == 2:
			btn_cora3.draw(screen, btn_corasound)
			btn_cora2.draw(screen, btn_corasound)
		elif vidas == 1:
			btn_cora3.draw(screen, btn_corasound)
		elif vidas == 0:
			menu_state = "main"	

		btn1 = buttontext.Button_Text(150, 200, f"{val_resta2[lista[0]]}")
		btn2 = buttontext.Button_Text(450, 200, f"{val_resta2[lista[1]]}")
		btn3 = buttontext.Button_Text(150, 350, f"{val_resta2[lista[2]]}")
		btn4 = buttontext.Button_Text(450, 350, f"{val_resta2[lista[3]]}")

		draw_text("¿Cual es el resultado de esta resta?", font2, TEXT_COL, 145, 50)
		if val_resta2[0] > val_resta2[1]:
			draw_text(f"{val_resta2[0]} - {val_resta2[1]}", font2, TEXT_COL, 250, 100)
		else:
			draw_text(f"{val_resta2[1]} - {val_resta2[0]}", font2, TEXT_COL, 250, 100)

		if btn1.drawtxt(screen) and clicked == False:
			if val_resta2[lista[0]] == val_resta2[2]:
				btn_correct.play()
				time.sleep(0.15)
			else:
				btn_incorrect.play()
				vidas = vidas - 1
			clicked = True
			random.shuffle(lista)
			val_resta2 = funciones.resta(2)

		if btn2.drawtxt(screen) and clicked == False:
			if val_resta2[lista[1]] == val_resta2[2]:
				btn_correct.play()
				time.sleep(0.15)
			else:
				btn_incorrect.play()
				vidas = vidas - 1
			clicked = True
			random.shuffle(lista)
			val_resta2 = funciones.resta(2)

		if btn3.drawtxt(screen) and clicked == False:
			if val_resta2[lista[2]] == val_resta2[2]:
				btn_correct.play()
				time.sleep(0.15)
			else:
				btn_incorrect.play()
				vidas = vidas - 1
			clicked = True
			random.shuffle(lista)
			val_resta2 = funciones.resta(2)

		if btn4.drawtxt(screen) and clicked == False:
			if val_resta2[lista[3]] == val_resta2[2]:
				btn_correct.play()
				time.sleep(0.15)
			else:
				btn_incorrect.play()
				vidas = vidas - 1
			clicked = True
			random.shuffle(lista)
			val_resta2 = funciones.resta(2)

		if btn_return.draw(screen, bnt_sound):
			random.shuffle(lista)
			val_resta2 = funciones.resta(2)
			menu_state = "niveles_resta"

#nivel 3 resta
	elif menu_state == "resta3":
		if vidas == 3:
			btn_cora1.draw(screen, btn_corasound)
			btn_cora2.draw(screen, btn_corasound)
			btn_cora3.draw(screen, btn_corasound)
		elif vidas == 2:
			btn_cora3.draw(screen, btn_corasound)
			btn_cora2.draw(screen, btn_corasound)
		elif vidas == 1:
			btn_cora3.draw(screen, btn_corasound)
		elif vidas == 0:
			menu_state = "main"	

		btn1 = buttontext.Button_Text(150, 200, f"{val_resta3[lista[0]]}")
		btn2 = buttontext.Button_Text(450, 200, f"{val_resta3[lista[1]]}")
		btn3 = buttontext.Button_Text(150, 350, f"{val_resta3[lista[2]]}")
		btn4 = buttontext.Button_Text(450, 350, f"{val_resta3[lista[3]]}")

		draw_text("¿Cual es el resultado de esta resta?", font2, TEXT_COL, 145, 50)
		if val_resta3[0] > val_resta3[1]:
			draw_text(f"{val_resta3[0]} - {val_resta3[1]}", font2, TEXT_COL, 250, 100)
		else:
			draw_text(f"{val_resta3[1]} - {val_resta3[0]}", font2, TEXT_COL, 250, 100)

		if btn1.drawtxt(screen) and clicked == False:
			if val_resta3[lista[0]] == val_resta3[2]:
				btn_correct.play()
				time.sleep(0.15)
			else:
				btn_incorrect.play()
				vidas = vidas - 1
			clicked = True
			random.shuffle(lista)
			val_resta3 = funciones.resta(3)

		if btn2.drawtxt(screen) and clicked == False:
			if val_resta3[lista[1]] == val_resta3[2]:
				btn_correct.play()
				time.sleep(0.15)
			else:
				btn_incorrect.play()
				vidas = vidas - 1
			clicked = True
			random.shuffle(lista)
			val_resta3 = funciones.resta(3)

		if btn3.drawtxt(screen) and clicked == False:
			if val_resta3[lista[2]] == val_resta3[2]:
				btn_correct.play()
				time.sleep(0.15)
			else:
				btn_incorrect.play()
				vidas = vidas - 1
			clicked = True
			random.shuffle(lista)
			val_resta3 = funciones.resta(3)

		if btn4.drawtxt(screen) and clicked == False:
			if val_resta3[lista[3]] == val_resta3[2]:
				btn_correct.play()
				time.sleep(0.15)
			else:
				btn_incorrect.play()
				vidas = vidas - 1
			clicked = True
			random.shuffle(lista)
			val_resta3 = funciones.resta(3)

		if btn_return.draw(screen, bnt_sound):
			random.shuffle(lista)
			val_resta3 = funciones.resta(3)
			menu_state = "niveles_resta"

#nivel 1 multiplicacion
	elif menu_state == "multi1":
		if vidas == 3:
			btn_cora1.draw(screen, btn_corasound)
			btn_cora2.draw(screen, btn_corasound)
			btn_cora3.draw(screen, btn_corasound)
		elif vidas == 2:
			btn_cora3.draw(screen, btn_corasound)
			btn_cora2.draw(screen, btn_corasound)
		elif vidas == 1:
			btn_cora3.draw(screen, btn_corasound)
		elif vidas == 0:
			menu_state = "main"	

		btn1 = buttontext.Button_Text(150, 200, f"{val_multi1[lista[0]]}")
		btn2 = buttontext.Button_Text(450, 200, f"{val_multi1[lista[1]]}")
		btn3 = buttontext.Button_Text(150, 350, f"{val_multi1[lista[2]]}")
		btn4 = buttontext.Button_Text(450, 350, f"{val_multi1[lista[3]]}")

		draw_text("¿Cual es el resultado de esta multiplicacion?", font2, TEXT_COL, 145, 50)
		draw_text(f"{val_multi1[0]} x {val_multi1[1]}", font2, TEXT_COL, 250, 100)

		if btn1.drawtxt(screen) and clicked == False:
			if val_multi1[lista[0]] == val_multi1[2]:
				btn_correct.play()
				time.sleep(0.15)
			else:
				btn_incorrect.play()
				vidas = vidas - 1
			clicked = True
			random.shuffle(lista)
			val_multi1 = funciones.multi(1)

		if btn2.drawtxt(screen) and clicked == False:
			if val_multi1[lista[1]] == val_multi1[2]:
				btn_correct.play()
				time.sleep(0.15)
			else:
				btn_incorrect.play()
				vidas = vidas - 1
			clicked = True
			random.shuffle(lista)
			val_multi1 = funciones.multi(1)

		if btn3.drawtxt(screen) and clicked == False:
			if val_multi1[lista[2]] == val_multi1[2]:
				btn_correct.play()
				time.sleep(0.15)
			else:
				btn_incorrect.play()
				vidas = vidas - 1
			clicked = True
			random.shuffle(lista)
			val_multi1 = funciones.multi(1)

		if btn4.drawtxt(screen) and clicked == False:
			if val_multi1[lista[3]] == val_multi1[2]:
				btn_correct.play()
				time.sleep(0.15)
			else:
				btn_incorrect.play()
				vidas = vidas - 1
			clicked = True
			random.shuffle(lista)
			val_multi1 = funciones.multi(1)

		if btn_return.draw(screen, bnt_sound):
			random.shuffle(lista)
			val_multi1 = funciones.multi(1)
			menu_state = "niveles_multi"

#nivel 2 multiplicacion	
	elif menu_state == "multi2":
		if vidas == 3:
			btn_cora1.draw(screen, btn_corasound)
			btn_cora2.draw(screen, btn_corasound)
			btn_cora3.draw(screen, btn_corasound)
		elif vidas == 2:
			btn_cora3.draw(screen, btn_corasound)
			btn_cora2.draw(screen, btn_corasound)
		elif vidas == 1:
			btn_cora3.draw(screen, btn_corasound)
		elif vidas == 0:
			menu_state = "main"	

		btn1 = buttontext.Button_Text(150, 200, f"{val_multi2[lista[0]]}")
		btn2 = buttontext.Button_Text(450, 200, f"{val_multi2[lista[1]]}")
		btn3 = buttontext.Button_Text(150, 350, f"{val_multi2[lista[2]]}")
		btn4 = buttontext.Button_Text(450, 350, f"{val_multi2[lista[3]]}")

		draw_text("¿Cual es el resultado de esta multiplicacion?", font2, TEXT_COL, 145, 50)
		draw_text(f"{val_multi2[0]} x {val_multi2[1]}", font2, TEXT_COL, 250, 100)

		if btn1.drawtxt(screen) and clicked == False:
			if val_multi2[lista[0]] == val_multi2[2]:
				btn_correct.play()
				time.sleep(0.15)
			else:
				btn_incorrect.play()
				vidas = vidas - 1
			clicked = True
			random.shuffle(lista)
			val_multi2 = funciones.multi(2)

		if btn2.drawtxt(screen) and clicked == False:
			if val_multi2[lista[1]] == val_multi2[2]:
				btn_correct.play()
				time.sleep(0.15)
			else:
				btn_incorrect.play()
				vidas = vidas - 1
			clicked = True
			random.shuffle(lista)
			val_multi2 = funciones.multi(2)

		if btn3.drawtxt(screen) and clicked == False:
			if val_multi2[lista[2]] == val_multi2[2]:
				btn_correct.play()
				time.sleep(0.15)
			else:
				btn_incorrect.play()
				vidas = vidas - 1
			clicked = True
			random.shuffle(lista)
			val_multi2 = funciones.multi(2)

		if btn4.drawtxt(screen) and clicked == False:
			if val_multi2[lista[3]] == val_multi2[2]:
				btn_correct.play()
				time.sleep(0.15)
			else:
				btn_incorrect.play()
				vidas = vidas - 1
			clicked = True
			random.shuffle(lista)
			val_multi2 = funciones.multi(2)

		if btn_return.draw(screen, bnt_sound):
			random.shuffle(lista)
			val_multi2 = funciones.multi(2)
			menu_state = "niveles_multi"

#nivel 3 multiplicacion
	elif menu_state == "multi3":
		if vidas == 3:
			btn_cora1.draw(screen, btn_corasound)
			btn_cora2.draw(screen, btn_corasound)
			btn_cora3.draw(screen, btn_corasound)
		elif vidas == 2:
			btn_cora3.draw(screen, btn_corasound)
			btn_cora2.draw(screen, btn_corasound)
		elif vidas == 1:
			btn_cora3.draw(screen, btn_corasound)
		elif vidas == 0:
			menu_state = "main"	

		btn1 = buttontext.Button_Text(150, 200, f"{val_multi3[lista[0]]}")
		btn2 = buttontext.Button_Text(450, 200, f"{val_multi3[lista[1]]}")
		btn3 = buttontext.Button_Text(150, 350, f"{val_multi3[lista[2]]}")
		btn4 = buttontext.Button_Text(450, 350, f"{val_multi3[lista[3]]}")

		draw_text("¿Cual es el resultado de esta multiplicacion?", font2, TEXT_COL, 145, 50)
		draw_text(f"{val_multi3[0]} x {val_multi3[1]}", font2, TEXT_COL, 250, 100)

		if btn1.drawtxt(screen) and clicked == False:
			if val_multi3[lista[0]] == val_multi3[2]:
				btn_correct.play()
				time.sleep(0.15)
			else:
				btn_incorrect.play()
				vidas = vidas - 1
			clicked = True
			random.shuffle(lista)
			val_multi3 = funciones.multi(3)

		if btn2.drawtxt(screen) and clicked == False:
			if val_multi3[lista[1]] == val_multi3[2]:
				btn_correct.play()
				time.sleep(0.15)
			else:
				btn_incorrect.play()
				vidas = vidas - 1
			clicked = True
			random.shuffle(lista)
			val_multi3 = funciones.multi(3)

		if btn3.drawtxt(screen) and clicked == False:
			if val_multi3[lista[2]] == val_multi3[2]:
				btn_correct.play()
				time.sleep(0.15)
			else:
				btn_incorrect.play()
				vidas = vidas - 1
			clicked = True
			random.shuffle(lista)
			val_multi3 = funciones.multi(3)

		if btn4.drawtxt(screen) and clicked == False:
			if val_multi3[lista[3]] == val_multi3[2]:
				btn_correct.play()
				time.sleep(0.15)
			else:
				btn_incorrect.play()
				vidas = vidas - 1
			clicked = True
			random.shuffle(lista)
			val_multi3 = funciones.multi(3)

		if btn_return.draw(screen, bnt_sound):
			random.shuffle(lista)
			val_multi3 = funciones.multi(3)
			menu_state = "niveles_multi"
		
#nivel 1 division	
	elif menu_state == "divi1":
		if vidas == 3:
			btn_cora1.draw(screen, btn_corasound)
			btn_cora2.draw(screen, btn_corasound)
			btn_cora3.draw(screen, btn_corasound)
		elif vidas == 2:
			btn_cora3.draw(screen, btn_corasound)
			btn_cora2.draw(screen, btn_corasound)
		elif vidas == 1:
			btn_cora3.draw(screen, btn_corasound)
		elif vidas == 0:
			menu_state = "main"	

		btn1 = buttontext.Button_Text(150, 200, f"{val_divi1[lista[0]]}")
		btn2 = buttontext.Button_Text(450, 200, f"{val_divi1[lista[1]]}")
		btn3 = buttontext.Button_Text(150, 350, f"{val_divi1[lista[2]]}")
		btn4 = buttontext.Button_Text(450, 350, f"{val_divi1[lista[3]]}")

		draw_text("¿Cual es el resultado de esta division?", font2, TEXT_COL, 145, 50)
		draw_text(f"{val_divi1[0]} {chr(247)} {val_divi1[1]}", font2, TEXT_COL, 250, 100)

		if btn1.drawtxt(screen) and clicked == False:
			if val_divi1[lista[0]] == val_divi1[2]:
				btn_correct.play()
				time.sleep(0.15)
			else:
				btn_incorrect.play()
				vidas = vidas - 1
			clicked = True
			random.shuffle(lista)
			val_divi1 = funciones.divi(1)

		if btn2.drawtxt(screen) and clicked == False:
			if val_divi1[lista[1]] == val_divi1[2]:
				btn_correct.play()
				time.sleep(0.15)
			else:
				btn_incorrect.play()
				vidas = vidas - 1
			clicked = True
			random.shuffle(lista)
			val_divi1 = funciones.divi(1)

		if btn3.drawtxt(screen) and clicked == False:
			if val_divi1[lista[2]] == val_divi1[2]:
				btn_correct.play()
				time.sleep(0.15)
			else:
				btn_incorrect.play()
				vidas = vidas - 1
			clicked = True
			random.shuffle(lista)
			val_divi1 = funciones.divi(1)

		if btn4.drawtxt(screen) and clicked == False:
			if val_divi1[lista[3]] == val_divi1[2]:
				btn_correct.play()
				time.sleep(0.15)
			else:
				btn_incorrect.play()
				vidas = vidas - 1
			clicked = True
			random.shuffle(lista)
			val_divi1 = funciones.divi(1)

		if btn_return.draw(screen, bnt_sound):
			random.shuffle(lista)
			val_divi1 = funciones.divi(1)
			menu_state = "niveles_divi"

#nivel 2 division	
	elif menu_state == "divi2":
		if vidas == 3:
			btn_cora1.draw(screen, btn_corasound)
			btn_cora2.draw(screen, btn_corasound)
			btn_cora3.draw(screen, btn_corasound)
		elif vidas == 2:
			btn_cora3.draw(screen, btn_corasound)
			btn_cora2.draw(screen, btn_corasound)
		elif vidas == 1:
			btn_cora3.draw(screen, btn_corasound)
		elif vidas == 0:
			menu_state = "main"	

		btn1 = buttontext.Button_Text(150, 200, f"{val_divi2[lista[0]]}")
		btn2 = buttontext.Button_Text(450, 200, f"{val_divi2[lista[1]]}")
		btn3 = buttontext.Button_Text(150, 350, f"{val_divi2[lista[2]]}")
		btn4 = buttontext.Button_Text(450, 350, f"{val_divi2[lista[3]]}")

		draw_text("¿Cual es el resultado de esta division?", font2, TEXT_COL, 145, 50)
		draw_text(f"{val_divi2[0]} {chr(247)} {val_divi2[1]}", font2, TEXT_COL, 250, 100)

		if btn1.drawtxt(screen) and clicked == False:
			if val_divi2[lista[0]] == val_divi2[2]:
				btn_correct.play()
				time.sleep(0.15)
			else:
				btn_incorrect.play()
				vidas = vidas - 1
			clicked = True
			random.shuffle(lista)
			val_divi2 = funciones.divi(2)

		if btn2.drawtxt(screen) and clicked == False:
			if val_divi2[lista[1]] == val_divi2[2]:
				btn_correct.play()
				time.sleep(0.15)
			else:
				btn_incorrect.play()
				vidas = vidas - 1
			clicked = True
			random.shuffle(lista)
			val_divi2 = funciones.divi(2)

		if btn3.drawtxt(screen) and clicked == False:
			if val_divi2[lista[2]] == val_divi2[2]:
				btn_correct.play()
				time.sleep(0.15)
			else:
				btn_incorrect.play()
				vidas = vidas - 1
			clicked = True
			random.shuffle(lista)
			val_divi2 = funciones.divi(2)

		if btn4.drawtxt(screen) and clicked == False:
			if val_divi2[lista[3]] == val_divi2[2]:
				btn_correct.play()
				time.sleep(0.15)
			else:
				btn_incorrect.play()
				vidas = vidas - 1
			clicked = True
			random.shuffle(lista)
			val_divi2 = funciones.divi(2)

		if btn_return.draw(screen, bnt_sound):
			random.shuffle(lista)
			val_divi2 = funciones.divi(2)
			menu_state = "niveles_divi"

#nivel 3 division	
	elif menu_state == "divi3":
		if vidas == 3:
			btn_cora1.draw(screen, btn_corasound)
			btn_cora2.draw(screen, btn_corasound)
			btn_cora3.draw(screen, btn_corasound)
		elif vidas == 2:
			btn_cora3.draw(screen, btn_corasound)
			btn_cora2.draw(screen, btn_corasound)
		elif vidas == 1:
			btn_cora3.draw(screen, btn_corasound)
		elif vidas == 0:
			menu_state = "main"	

		btn1 = buttontext.Button_Text(150, 200, f"{val_divi3[lista[0]]}")
		btn2 = buttontext.Button_Text(450, 200, f"{val_divi3[lista[1]]}")
		btn3 = buttontext.Button_Text(150, 350, f"{val_divi3[lista[2]]}")
		btn4 = buttontext.Button_Text(450, 350, f"{val_divi3[lista[3]]}")

		draw_text("¿Cual es el resultado de esta division?", font2, TEXT_COL, 145, 50)
		draw_text(f"{val_divi3[0]} {chr(247)} {val_divi3[1]}", font2, TEXT_COL, 250, 100)

		if btn1.drawtxt(screen) and clicked == False:
			if val_divi3[lista[0]] == val_divi3[2]:
				btn_correct.play()
				time.sleep(0.15)
			else:
				btn_incorrect.play()
				vidas = vidas - 1
			clicked = True
			random.shuffle(lista)
			val_divi3 = funciones.divi(3)

		if btn2.drawtxt(screen) and clicked == False:
			if val_divi3[lista[1]] == val_divi3[2]:
				btn_correct.play()
				time.sleep(0.15)
			else:
				btn_incorrect.play()
				vidas = vidas - 1
			clicked = True
			random.shuffle(lista)
			val_divi3 = funciones.divi(3)

		if btn3.drawtxt(screen) and clicked == False:
			if val_divi3[lista[2]] == val_divi3[2]:
				btn_correct.play()
				time.sleep(0.15)
			else:
				btn_incorrect.play()
				vidas = vidas - 1
			clicked = True
			random.shuffle(lista)
			val_divi3 = funciones.divi(3)

		if btn4.drawtxt(screen) and clicked == False:
			if val_divi3[lista[3]] == val_divi3[2]:
				btn_correct.play()
				time.sleep(0.15)
			else:
				btn_incorrect.play()
				vidas = vidas - 1
			clicked = True
			random.shuffle(lista)
			val_divi3 = funciones.divi(3)

		if btn_return.draw(screen, bnt_sound):
			random.shuffle(lista)
			val_divi3 = funciones.divi(3)
			menu_state = "niveles_divi"

#Controlador de eventos	
	for event in pygame.event.get():

		if event.type == pygame.MOUSEBUTTONUP:
			clicked = False

		if event.type == pygame.QUIT:
			run = False

		if menu_state == "main":	
			if event.type == pygame.KEYDOWN:
				print(event.key)
				if event.key == 113 or event.key == 27:
					run = False
	pygame.display.update()

pygame.quit()
