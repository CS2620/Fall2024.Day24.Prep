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