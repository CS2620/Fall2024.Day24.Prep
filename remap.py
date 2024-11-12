import math

def color_distance(one, two):
    r_diff = one[0] - two[0]
    g_diff = one[1] - two[1]
    b_diff = one[2] - two[2]

    # return abs(r_diff)+abs(g_diff)+abs(b_diff)
    return math.sqrt((r_diff)**2+(g_diff)**2+(b_diff)**2)


def remap(image, data, palette, filename):

  print("Building cluster distance matrix")
  palette_distances = []
  for color1 in palette:
      row = []
      for color2 in palette:
          distance = color_distance(color1, color2)
          row.append(distance)
      palette_distances.append(row)

  
  for y in range(image.height):
    for x in range(image.width):
      pixel = data[x,y]
      min_distance = 442
      min_index = 0
      for i,color in enumerate(palette):
        palette_distance = palette_distances[min_index][i]
        if palette_distance > min_distance * 2:
           continue

        distance = color_distance(color, pixel)
        if distance < min_distance:
          min_distance = distance
          min_index = i
      
      data[x,y] = palette[min_index]

      
  image.save(filename)

def remap_dither(image, data, palette, filename):
    print("Building cluster distance matrix")
    palette_distances = []
    for color1 in palette:
        row = []
        for color2 in palette:
            distance = color_distance(color1, color2)
            row.append(distance)
        palette_distances.append(row)

    errors = []
    for x in range(image.width):
      column = []
      for y in range(image.height):
        column.append(0)
      errors.append(column)
       

    for y in range(image.height):
      error_r = 0
      error_g = 0
      error_b = 0
      for x in range(image.width):
        pixel = data[x,y]
        current_color = (pixel[0] - error_r, pixel[1] - error_g, pixel[2] - error_b)
        min_distance = 442000
        min_index = 0
        for i,color in enumerate(palette):
          palette_distance = palette_distances[min_index][i]
          if palette_distance > min_distance * 2:
            continue

          distance = color_distance(color, current_color)
          if distance < min_distance:
            min_distance = distance
            min_index = i
        
        palette_color = palette[min_index]

        this_error_r = palette_color[0]-current_color[0]
        this_error_g = palette_color[1]-current_color[1]
        this_error_b = palette_color[2]-current_color[2]


        error_r = this_error_r
        error_g = this_error_g
        error_b = this_error_b

        data[x,y] = palette[min_index]

        
    image.save(filename)