from vec3 import vec3 as color
from ray import ray as Ray
# import vec3
import vec3
# import math
import math
from hittable import hit_record

# Importing interval
from interval import interval

import material
# Functions for finding pixel values


def linear_to_gama(linear_component):
    return math.sqrt(linear_component)


def ray_color(ray, world, depth):
    record = hit_record()

    if depth <= 0:
        return color([0, 0, 0])
    if (world.hit(ray, interval(0.001, float('inf')), record)):

        scattered = Ray()
        attenuation = color([0, 0, 0])
        if isinstance(record.mat, material.dielectric):
            attenuation = color([1.0, 1.0, 1.0])
    # Add more conditions for other material types as needed
        if (record.mat.scatter(ray, record, attenuation, scattered)):

            return attenuation * ray_color(scattered, world, depth-1)
        return color([0, 0, 0])

    unit_direction = vec3.unit_vector(ray.get_direction())
    a = 0.5*(unit_direction.y() + 1.0)
    return (1.0 - a) * color([1, 1, 1]) + a*color([0.5, 0.7, 1.0])


def write_color(image, pixel_color, i, j, samples_per_pixel):

    r = pixel_color.x()
    g = pixel_color.y()
    b = pixel_color.z()

    scale = 1.0 / samples_per_pixel
    r *= scale
    g *= scale
    b *= scale

    r = linear_to_gama(r)
    g = linear_to_gama(g)
    b = linear_to_gama(b)

    intensity = interval(0.000, 0.999)

    image.putpixel((j, i), (
        int(256 * intensity.clamp(r)),
        int(256 * intensity.clamp(g)),
        int(256 * intensity.clamp(b))
    ))
