from pico2d import *
import math

open_canvas()

# fill here
grass = load_image('grass.png')
character = load_image('character.png')

origin_x = 400
origin_y = 90
canvas_width = 800
canvas_height = 600
x = 400
y = 90

def rectangle_move():
	global x
	global y
	global character
	global grass

	y = 90
	while (x < 800):
		clear_canvas_now()
		grass.draw_now(400, 30)
		character.draw_now(x, y)
		x = x + 2
		delay(0.01)

	while (y < 600):
		clear_canvas_now()
		grass.draw_now(400, 30)
		character.draw_now(x, y)
		y = y + 2
		delay(0.01)

	while (x > 0):
		clear_canvas_now()
		grass.draw_now(400, 30)
		character.draw_now(x, y)
		x = x - 2
		delay(0.01)

	while (y > 90):
		clear_canvas_now()
		grass.draw_now(400, 30)
		character.draw_now(x, y)
		y = y - 2
		delay(0.01)

	while (x < 400):
		clear_canvas_now()
		grass.draw_now(400, 30)
		character.draw_now(x, y)
		x = x + 2
		delay(0.01)


def circle_move():
        angle = 0
        global x
        global y
        global character
        global grass
        x = 400
        y = 90
        for angle in range(90, 450):
                clear_canvas_now()
                grass.draw_now(400, 30)
                character.draw_now(x, y)
                x = x + 4 * math.sin(angle / 360 * 2 * math.pi)
                y = y - 4 * math.cos(angle / 360 * 2 * math.pi)

while (True):
        rectangle_move()
        circle_move()



close_canvas()
