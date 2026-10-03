###This code will not work in repl.it as there is no access to the colorgram package here.###
##We talk about this in the video tutorials##
import colorgram
import os

dir_path = os.path.dirname(__file__)
image_path = os.path.join(dir_path, "image.jpg")

rgb_colors = []
colors = colorgram.extract("image_path", 30)
for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    new_color =(r, g, b)
    rgb_colors.append(new_color)
    
print(rgb_colors) 