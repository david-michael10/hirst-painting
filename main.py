import colorgram

colors = colorgram.extract("image.jpg", 20)

color_list = []
for i in colors:
    red = i.rgb.r
    green = i.rgb.g
    blue = i.rgb.b
    color_tuple = (red, green, blue)
    color_list.append(color_tuple)

print(color_list)