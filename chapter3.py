import arcade

arcade.open_window( 600, 600, "Drawing Example")

# Set the background color
arcade.set_background_color(arcade.color.AIR_SUPERIORITY_BLUE)

arcade.start_render()

# --- Draw the background view ---

# Draw the ground 
arcade.draw_lrtb_rectangle_filled(0, 800, 200, 0, arcade.color.DARK_SEA_GREEN)

# Draw the sun
arcade.draw_circle_filled(600, 600, 75, arcade.color.YELLOW_ROSE)

# Draw two trees 
arcade.draw_lrtb_rectangle_filled(85, 100, 250, 200, arcade.color.DARK_BROWN)
arcade.draw_triangle_filled(40, 250, 140, 250, 85, 400, arcade.color.DARK_GREEN)

arcade.draw_lrtb_rectangle_filled(495, 510, 250, 200,  arcade.color.DARK_BROWN)
arcade.draw_triangle_filled(445, 250, 555, 250, 500, 400, arcade.color.DARK_GREEN)

# --- Draw the body of the figure ---

# Draw a circle for the base 
arcade.draw_circle_filled(300, 150, 100, arcade.color.WHITE_SMOKE)

# Draw a circle for the body
arcade.draw_circle_filled(300, 275, 75, arcade.color.WHITE_SMOKE)

# Draw a circle for the head
arcade.draw_circle_filled(300, 375, 60, arcade.color.WHITE_SMOKE)

# --- Draw the features for the figure ---

# Draw the buttons
arcade.draw_circle_filled(300, 235, 8, arcade.color.DEEP_CHESTNUT)
arcade.draw_circle_filled(300, 235, 3, arcade.color.BLACK)

arcade.draw_circle_filled(300, 265, 8, arcade.color.DEEP_CHESTNUT)
arcade.draw_circle_filled(300, 265, 3, arcade.color.BLACK)

arcade.draw_circle_filled(300, 295, 8, arcade.color.DEEP_CHESTNUT)
arcade.draw_circle_filled(300, 295, 3, arcade.color.BLACK)

# Draw the eyes
arcade.draw_triangle_filled(265, 385, 285, 385, 275, 395, arcade.color.BLACK)

arcade.draw_triangle_filled(315, 385, 335, 385, 325, 395, arcade.color.BLACK)

# Draw the nose
arcade.draw_triangle_filled(295, 365, 350, 365, 295, 375, arcade.color.ORANGE_PEEL)

# Draw the mouth
arcade.draw_ellipse_filled(300, 350, 35, 20, arcade.color.BLACK, 0, 30)

# Draw the arms
arcade.draw_line(375, 265, 410, 345, arcade.color.DARK_BROWN, 3)

arcade.draw_line(225, 265, 190, 345, arcade.color.DARK_BROWN, 3)

# Draw a hat
arcade.draw_rectangle_filled(300, 480, 80, 95, arcade.color.DEEP_CHESTNUT, 0)
arcade.draw_ellipse_filled(300, 435, 130, 55, arcade.color.DEEP_LILAC, 0, 50)


arcade.finish_render()

arcade.run()

