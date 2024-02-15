# Necessary Classes
from interval import interval
from ray import ray
from vec3 import vec3 as point3
import vec3

from hittable import hittable
from hittable import hit_record

from utility import degrees_to_radians
import math

import color
from color import color as col
import random

# Importing Utility Functions from main
from utility import random_float
# For ppm Image
from PIL import Image


class camera:
    def __init__(self):
        self.image_height = 0

    # Creating Image
    aspect_ratio = 16.0 / 9.0
    image_width = 400
    # max_depth taken 50 in lesson for faster code 10 is used
    max_depth = 10

    # Samples_per_pixel taken 100 in the lesson for faster code 10 is used
    samples_per_pixel = 10

    #  Vertical view angle (field of view)
    vfov = 90

    lookfrom = point3([-2, 2, 1])  # Point camera is looking from
    lookat = point3([0, 0, -1])   # Point camera is looking at
    vup = point3([0, 1, 0])     # Camera-relative "up" direction

    camera_center = point3([0, 0, 0])
    pixel_delta_u = point3([0, 0, 0])
    pixel_delta_u = point3([0, 0, 0])
    pixel00_loc = point3([0, 0, 0])

    def initialize(self):
        self.image_height = int(self.image_width/self.aspect_ratio)
        self.image_height = max(1, self.image_height)

        self.camera_center = self.lookfrom
        # Camera
        focal_length = (self.lookfrom - self.lookat).length()
        theta = degrees_to_radians(self.vfov)
        h = math.tan(theta/2)

        viewport_height = 2.0 * h * focal_length
        viewport_width = (viewport_height *
                          (float(self.image_width) / self.image_height))

        w = vec3.unit_vector(self.lookfrom - self.lookat)
        u = vec3.unit_vector(vec3.cross(self.vup, w))
        v = vec3.cross(w, u)

        # Calculate the vectors across the horizontal and down the vertical viewport edges.
        viewport_u = viewport_width * u
        viewport_v = viewport_height * -v

        # Deltas
        self.pixel_delta_u = viewport_u / self.image_width
        self.pixel_delta_v = viewport_v / self.image_height

        # Finding starting point (Upper left pixel)

        viewport_upper_left = self.camera_center - \
            (focal_length * w) - viewport_u/2 - viewport_v/2

        self.pixel00_loc = viewport_upper_left + \
            0.5 * (self.pixel_delta_u + self.pixel_delta_v)

    def pixel_sample_square(self):
        # Returns a random point in the square surrounding a pixel at the origin.
        px = -0.5 + random_float()
        py = -0.5 + random_float()

        return ((px * self.pixel_delta_u) + (py * self.pixel_delta_v))

    def get_ray(self, i, j):
        pixel_center = self.pixel00_loc + \
            (j * self.pixel_delta_u) + (i * self.pixel_delta_v)

        pixel_sample = pixel_center + self.pixel_sample_square()

        ray_origin = self.camera_center
        ray_direction = pixel_sample - ray_origin
        return ray(ray_origin, ray_direction)

    def render(self, world):
        self.initialize()
        print("P3\n" + str(self.image_width) +
              " " + str(self.image_height) + "\n255\n")
        img = Image.new(
            'RGB', (self.image_width, self.image_height), color='white')

        for i in range(self.image_height):
            print("\rScanlines remaining : " + str(self.image_height-i) + " ")
            for j in range(self.image_width):
                pixel_color = col([0, 0, 0])
                for sample in range(self.samples_per_pixel):
                    r = self.get_ray(i, j)

                    pixel_color += color.ray_color(r, world, self.max_depth)

                color.write_color(img, pixel_color, i, j,
                                  self.samples_per_pixel)

        print("\rDone                 \n")
        img.save("deneme.ppm", format='PPM')
