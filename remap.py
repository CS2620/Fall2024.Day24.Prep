import math

def remap(image, data, palette, filename):
 
  def color_distance(one, two):
    r_diff = one[0] - two[0]
    g_diff = one[1] - two[1]
    b_diff = one[2] - two[2]

    return math.sqrt(r_diff**2+g_diff**2+b_diff**2)

  for y in range(image.height):
    for x in range(image.width):
      pixel = data[x,y]
      min_distance = 10000
      best_color = None
      for color in palette:
        distance = color_distance(color, pixel)
        if distance < min_distance:
          min_distance = distance
          best_color = color
      
      data[x,y] = best_color

      
  image.save(filename)