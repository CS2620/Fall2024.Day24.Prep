import math
from PIL import Image

def print_palette(entries, pixel_size, name):
  wrap_size = math.ceil(math.sqrt(len(entries)))
  image_out = Image.new("RGB", (wrap_size*pixel_size, pixel_size*math.ceil(len(entries)/wrap_size)))
  data_out = image_out.load()

  for index, pixel in enumerate(entries):
    pixel_start_x = (index%wrap_size)*pixel_size
    pixel_start_y = int(index/wrap_size)*pixel_size
    for y in range(pixel_size):
      for x in range(pixel_size):
        data_out[x + pixel_start_x, y + pixel_start_y] = pixel[0]

  image_out.save(name)