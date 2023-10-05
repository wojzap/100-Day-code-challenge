import colorgram


def get_colors(colors):
    list_of_colors = []
    for i in range(len(colors)):
        first_color = colors[i]
        red = first_color.rgb[0]
        green = first_color.rgb[1]
        blue = first_color.rgb[2]
        rgb = (red, green, blue)
        list_of_colors.append(rgb)

    return list_of_colors


extracted_colors = colorgram.extract("hirst-1.jpg", 20)
colors = get_colors(extracted_colors)
