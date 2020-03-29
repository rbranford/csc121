import arcade


SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600

FISH_WIDTH = 85
FISH_HEIGHT = 35


def draw_sand():
    arcade.draw_lrtb_rectangle_filled(0, SCREEN_WIDTH, SCREEN_HEIGHT / 3, 0, arcade.color.SANDSTORM)

def draw_fishr(x, y, color):
    # Fish facing right 

    # Body
    arcade.draw_ellipse_filled(x + 70, y + 15, 85, 35, color, 0, 50)
    arcade.draw_ellipse_outline(x + 70, y + 15, 85, 35, arcade.color.BLACK, 2, 0, 50)
    
    # Tail
    arcade.draw_triangle_filled(x, y - 5, x + 28, y + 15, x, y + 35, color)
    arcade.draw_triangle_outline(x, y - 5, x + 28, y + 15, x, y + 35, arcade.color.BLACK, 2)

    # Eyes and mouth
    arcade.draw_circle_filled(x + 94, y + 20, 5, arcade.color.WHITE_SMOKE, 50)
    arcade.draw_circle_filled(x + 96, y + 20, 3, arcade.color.BLACK, 50)
    arcade.draw_line(x + 98, y + 10, x + 110, y + 10, arcade.color.BLACK, 1)

def draw_fishl(x, y, color):
    # Fish facing left

    # Body
    arcade.draw_ellipse_filled(x + 70, y + 15, 85, 35, color, 0, 50)
    arcade.draw_ellipse_outline(x + 70, y + 15, 85, 35, arcade.color.BLACK, 2, 0, 50)

    # Tail
    arcade.draw_triangle_filled(x + 170, y, x + 112, y + 15, x + 170, y + 40, color)
    arcade.draw_triangle_outline(x + 170, y, x + 112, y + 15, x + 170, y + 40, arcade.color.BLACK, 2)

    # Eyes and mouth
    arcade.draw_circle_filled(x + 38, y + 20, 5, arcade.color.WHITE_SMOKE, 50)
    arcade.draw_circle_filled(x + 36, y + 20, 3, arcade.color.BLACK, 50)
    arcade.draw_line(x +30, y + 10, x + 45, y + 10, arcade.color.BLACK, 1)

def draw_smallfish(x, y, color):
    # School of fish

    # Body
    arcade.draw_ellipse_filled(x + 30, y + 15, 20, 15, color, 0, 50)
    arcade.draw_ellipse_outline(x + 30, y + 15, 20, 15, arcade.color.BLACK, 2, 0, 50)
    
    # Tail
    arcade.draw_triangle_filled(x, y + 5, x + 20, y + 15, x, y + 22, color)
    arcade.draw_triangle_outline(x, y + 5, x + 20, y + 15, x, y + 22, arcade.color.BLACK, 2)

    # Eyes
    arcade.draw_circle_filled(x + 33, y + 18, 2, arcade.color.WHITE_SMOKE, 50)
    arcade.draw_circle_filled(x + 35, y + 18, 1, arcade.color.BLACK, 50)

    # Body
    arcade.draw_ellipse_filled(x + 50, y + 35, 20, 15, color, 0, 50)
    arcade.draw_ellipse_outline(x + 50, y + 35, 20, 15, arcade.color.BLACK, 2, 0, 50)
    
    # Tail
    arcade.draw_triangle_filled(x + 20, y + 25, x + 40, y + 35, x + 20, y + 42, color)
    arcade.draw_triangle_outline(x + 20, y + 25, x + 40, y + 35, x + 20, y + 42, arcade.color.BLACK, 2)

    # Eyes
    arcade.draw_circle_filled(x + 53, y + 38, 2, arcade.color.WHITE_SMOKE, 50)
    arcade.draw_circle_filled(x + 55, y + 38, 1, arcade.color.BLACK, 50)

    # Body
    arcade.draw_ellipse_filled(x + 10, y - 5, 20, 15, color, 0, 50)
    arcade.draw_ellipse_outline(x + 10, y - 5, 20, 15, arcade.color.BLACK, 2, 0, 50)
    
    # Tail
    arcade.draw_triangle_filled(x - 20, y - 15, x, y - 5, x - 20, y + 2, color)
    arcade.draw_triangle_outline(x - 20, y - 15, x, y - 5, x - 20, y + 2, arcade.color.BLACK, 2)

    # Eyes
    arcade.draw_circle_filled(x + 13, y - 2, 2, arcade.color.WHITE_SMOKE, 50)
    arcade.draw_circle_filled(x + 15, y - 2, 1, arcade.color.BLACK, 50)

    # Body
    arcade.draw_ellipse_filled(x + 80, y + 15, 20, 15, color, 0, 50)
    arcade.draw_ellipse_outline(x + 80, y + 15, 20, 15, arcade.color.BLACK, 2, 0, 50)
    
    # Tail
    arcade.draw_triangle_filled(x + 50, y + 5, x + 70, y + 15, x + 50, y + 22, color)
    arcade.draw_triangle_outline(x + 50, y + 5, x + 70, y + 15, x + 50, y + 22, arcade.color.BLACK, 2)

    # Eyes
    arcade.draw_circle_filled(x + 83, y + 18, 2, arcade.color.WHITE_SMOKE, 50)
    arcade.draw_circle_filled(x + 85, y + 18, 1, arcade.color.BLACK, 50)

    # Body
    arcade.draw_ellipse_filled(x + 55, y - 15, 20, 15, color, 0, 50)
    arcade.draw_ellipse_outline(x + 55, y - 15, 20, 15, arcade.color.BLACK, 2, 0, 50)
    
    # Tail
    arcade.draw_triangle_filled(x + 25, y - 25, x + 45, y - 15, x + 25, y - 8, color)
    arcade.draw_triangle_outline(x + 25, y - 25, x + 45, y - 15, x + 25, y - 8, arcade.color.BLACK, 2)

    # Eyes
    arcade.draw_circle_filled(x + 58, y - 12, 2, arcade.color.WHITE_SMOKE, 50)
    arcade.draw_circle_filled(x + 60, y - 12, 1, arcade.color.BLACK, 50)

def draw_vegetatianl(x, y):
    arcade.draw_triangle_filled(x, y + 200, x + 10, y + 200, x + 5, y + 250, arcade.color.GREEN)
    arcade.draw_lrtb_rectangle_filled(x, y + 10, x + 200, y, arcade.color.GREEN)
    
    arcade.draw_triangle_filled(x + 20, y + 100, x + 30, y + 100, x + 25, y + 150, arcade.color.GREEN)
    arcade.draw_lrtb_rectangle_filled(x + 20, y + 30, x + 100, y - 50, arcade.color.GREEN)
    
    arcade.draw_triangle_filled(x + 80, y + 150, x + 90, y + 150, x + 85, y + 175, arcade.color.GREEN)
    arcade.draw_lrtb_rectangle_filled(x + 80, y + 90, x + 150, y - 50, arcade.color.GREEN)
   
   
def draw_vegetatianr(x, y):
    arcade.draw_triangle_filled(440, 300, 450, 300, 445, 380, arcade.color.GREEN)
    arcade.draw_lrtb_rectangle_filled(440, 450, 300, 20, arcade.color.GREEN)

    arcade.draw_triangle_filled(410, 400, 420, 400, 415, 450, arcade.color.GREEN)
    arcade.draw_lrtb_rectangle_filled(410, 420, 400, 20, arcade.color.GREEN)
    
    arcade.draw_triangle_filled(390, 250, 400, 250, 395, 280, arcade.color.GREEN)
    arcade.draw_lrtb_rectangle_filled(390, 400, 250, 20, arcade.color.GREEN)

def draw_bubbles(x, y):
    arcade.draw_circle_outline(x + 230, y + 175, 5, arcade.color.BLACK, 2, 50)
    arcade.draw_circle_outline(x + 245, y + 190, 5, arcade.color.BLACK, 2, 50)
    arcade.draw_circle_outline(x + 260, y + 185, 5, arcade.color.BLACK, 2, 50)
    arcade.draw_circle_outline(x + 250, y + 210, 5, arcade.color.BLACK, 2, 50)

positions1 = {
    "x": 150, 
    "y": 150 
}

positions2 = {
    "x": 350,
    "y": 350
}

positions3 = {
    "x": 150, 
    "y": 50
}

positions4 = {
    "x": 0,
    "y": 0
}


def on_draw(delta_time):
    arcade.start_render()


    draw_sand()
    draw_vegetatianl(0, 0)
    draw_vegetatianl(60,60)

    draw_fishr(positions1["x"], positions1["y"], arcade.color.CHROME_YELLOW)
    draw_fishl(positions2["x"], positions2["y"], arcade.color.PURPLE_HEART)
    draw_smallfish(positions3["x"], positions3["y"], arcade.color.PINK_LAVENDER)
    draw_bubbles(positions4["x"], positions4["y"])

    draw_vegetatianr(0, 0)
    
    # lr (Left and Right), ud(Up and Down)
    speed_lr_one = 3
    speed_ud_one = 3
    positions1["x"] += speed_lr_one
    positions1["y"] += speed_ud_one

    speed_lr_two = 2
    speed_ud_two = 0
    positions2["x"] -= speed_lr_two
    positions2["y"] -= speed_ud_two

    speed_school_lr = 6
    speed_school_ud = 0
    positions3["x"] += speed_school_lr
    positions3["y"] += speed_school_ud

    speed_bubbles_lr = 1
    speed_bubbles_ud = 10
    positions4["x"] += speed_bubbles_lr
    positions4["y"] += speed_bubbles_ud
 

def main():
    arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, "Underwater")
    arcade.set_background_color(arcade.color.AQUAMARINE)

    arcade.schedule(on_draw, 1/60)

    arcade.run()

if __name__ == '__main__': 
    main()