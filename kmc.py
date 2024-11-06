from PIL import Image
import math
from get_palette import get_palette
from print_palette import print_palette
from remap import remap
from nes_palette import nes_palette
import random

next_random_color = 0
def random_color():
  # global next_random_color
  # next_random_color += 1
  # return nes_palette[next_random_color]
  return (int(random.random()*255), int(random.random()*255), int(random.random()*255))

def color_distance(one, two):
    r_diff = one[0] - two[0]
    g_diff = one[1] - two[1]
    b_diff = one[2] - two[2]

    return math.sqrt(r_diff**2+g_diff**2+b_diff**2)


print(random_color())

image = Image.open("cat.jpg")
data = image.load()

pixels = get_palette(image, data)

count_clusters = 16

k_means = []
for i in range(count_clusters):
  k_means += [random_color()]
  

print(k_means)

clusters = [[] for _ in range(count_clusters)]
print(clusters)

for pixel in pixels:
  min_distance = 10000
  min_cluster = -1
  for i in range(count_clusters):
    distance = color_distance(pixel[0], k_means[i])
    if distance < min_distance:
      min_distance = distance
      min_cluster = i
  clusters[min_cluster].append(pixel)

print(clusters[0][:10])

print(k_means)
for i in range(2):
  print("Update step " + str(i))
  # Now recenter the k_means
  for i in range(count_clusters):
    sum_r = 0 
    sum_g = 0
    sum_b = 0

    sum_frequencies = 0
    for pixel in clusters[i]:
      sum_r += pixel[0][0] * pixel[1]
      sum_g += pixel[0][1] * pixel[1]
      sum_b += pixel[0][2] * pixel[1]
      sum_frequencies += pixel[1]

    if sum_frequencies != 0:
      sum_r //= sum_frequencies
      sum_g //= sum_frequencies
      sum_b //= sum_frequencies

      k_means[i] = (sum_r, sum_g, sum_b)
    else:
      k_means[i] = random_color()

  print(k_means)

remap(image, data, k_means, "kmc_cat.png")


