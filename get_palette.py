def get_palette(image, data):
  pixel_frequency = dict()

  for y in range(image.height):
    for x in range(image.width):
      pixel = data[x,y]
      if pixel in pixel_frequency.keys():
        pixel_frequency[pixel] = pixel_frequency[pixel]+1
      else:
        pixel_frequency[pixel] = 1


  entries = sorted(pixel_frequency.items(), key=lambda pair:pair[1], reverse=True)
  return entries