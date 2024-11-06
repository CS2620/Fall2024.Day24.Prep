from PIL import Image
import math
from get_palette import get_palette
from print_palette import print_palette
from remap import remap
from nes_palette import nes_palette
import random



basic_palette = [
  (0,0,0),
  (64, 64, 64), 
  (128, 128, 128),
  (192, 192, 192),
  (255,255,255),
  (255, 0, 0),
  (0, 255, 0),
  (0, 0, 255),
  ]

def random_color():
    return (int(random.random()*255),int(random.random()*255),int(random.random()*255))

def color_distance(one, two):
    return math.sqrt((one[0]-two[0])**2+(one[1]-two[1])**2+(one[2]-two[2])**2)

image = Image.open("fish.jpg")
data = image.load()

entries = get_palette(image, data)

count_clusters = 256

cluster_centers = []

for i in range(count_clusters):
    cluster_centers.append(random_color())
    
# print(cluster_centers)

closest_pixels = [[] for i in range(count_clusters)]
# print(closest_pixels)

for _ in range(2):
    print("Step")
    for pixel in entries:
        min_distance = 100000
        min_index = -1
        for i in range(count_clusters):
            center = cluster_centers[i]
            distance = color_distance(pixel[0], center)
            if distance < min_distance:
                min_distance = distance
                min_index = i
        closest_pixels[min_index].append(pixel)
        
    # print(closest_pixels[0][:10])

    # Update the pixel centers
            
    for i in range(count_clusters):
        sum_r = 0
        sum_g = 0
        sum_b = 0
        
        pixel_count = 0
        for j in range(len(closest_pixels[i])):
            sum_r += closest_pixels[i][j][0][0]*closest_pixels[i][j][1]
            sum_g += closest_pixels[i][j][0][1]*closest_pixels[i][j][1]
            sum_b += closest_pixels[i][j][0][2]*closest_pixels[i][j][1]
            pixel_count += closest_pixels[i][j][1]
        if pixel_count > 0:
            sum_r //= pixel_count
            sum_g //= pixel_count
            sum_b //= pixel_count
            
            cluster_centers[i] = (sum_r, sum_g, sum_b)
        else:
            cluster_centers[i] = random_color()

print(cluster_centers)

remap(image, data, cluster_centers, "fish_kmc_2.png")
    

