# To sample less frequently than 100, set
# sub_sample_frequency to something less than 1

def get_palette(image, data, sub_sample_frequency = 1):
  pixel_frequency = dict()

  sum_sub_sample = 0


  for y in range(image.height):
    for x in range(image.width):
      sum_sub_sample += sub_sample_frequency
      if sum_sub_sample >= 1:
        pixel = data[x,y]
        if pixel in pixel_frequency.keys():
          pixel_frequency[pixel] = pixel_frequency[pixel]+1
        else:
          pixel_frequency[pixel] = 1
        sum_sub_sample-= 1
      


  entries = sorted(pixel_frequency.items(), key=lambda pair:pair[1], reverse=True)
  return entries