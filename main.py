# Importing hittable classes
from sphere import sphere
from hittable_list import hittable_list

from utility import random_float
from utility import random_of_float


import math
# Importing vec3 class and functions
from vec3 import vec3

from material import metal
from material import Lambertian
from material import dielectric

# Importing Camera
from camera import camera
world = hittable_list()

# ...

ground_material = Lambertian(vec3([0.5, 0.5, 0.5]))
world.add(sphere(vec3([0, -1000, 0]), 1000, ground_material))
material1= Lambertian(vec3([0.5,0.5,0.5]))

cam = camera()

cam.aspect_ratio = 16.0 / 9.0
cam.image_width = 1200
cam.samples_per_pixel = 10
cam.max_depth = 10

cam.vfov = 20
cam.lookfrom = vec3([13, 2, 3])
cam.lookat = vec3([0, 0, 0])
cam.vup = vec3([0, 1, 0])

camera.render(cam, world)
