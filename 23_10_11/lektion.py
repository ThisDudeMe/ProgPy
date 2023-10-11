









'''from PIL import Image
import random

# Define the width and height of the image
width = 500
height = 500

# Create a new image with RGB color mode
image = Image.new("RGB", (width, height))

# Create a pixel-by-pixel loop to set random RGB colors
for x in range(width):
    for y in range(height):
        # Check if the pixel is on the border (edge) of the image
        is_on_border = x == 0 or y == 0 or x == width - 1 or y == height - 1

        if is_on_border:
            # If it's on the border, set the color to green
            color = (0, 255, 0)
        else:
            neighbor_color_up = image.getpixel((x, y - 1))  # Get the color of the pixel above
            neighbor_color_left = image.getpixel((x - 1, y))  # Get the color of the pixel 1 to the left

            if neighbor_color_up == (255, 0, 0) and neighbor_color_left == (255, 0, 0):
                color = (255, 0, 0)  # If the pixel above and 1 to the left are red, set this pixel to red
            elif neighbor_color_up == (0, 0, 255) and neighbor_color_left == (0, 0, 255):
                color = (0, 0, 255)  # If the pixel above and 1 to the left are blue, set this pixel to blue
            else:
                neighbor_color_down = image.getpixel((x, y + 1))  # Get the color of the pixel 1 below
                if neighbor_color_up == (255, 0, 0):
                    color = (255, 0, 0)  # If the pixel above is red, set this pixel to red
                elif neighbor_color_up == (0, 0, 255):
                    color = (0, 0, 255)  # If the pixel above is blue, set this pixel to blue
                elif neighbor_color_down == (0, 255, 0):
                    color = (0, 255, 0)  # If 1 below is green, set this pixel to green
                else:
                    color = (0, 255, 0)  # Default to green

        image.putpixel((x, y), color)

# Show the image in a window
image.show()
'''