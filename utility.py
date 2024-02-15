import random
import math

pi = math.pi


def degrees_to_radians(degrees):
    return degrees * pi / 180.0


def random_float():
    # Returns random value between [0,1)
    return random.random()


def random_of_float(min, max):
    return min + (max-min)*random_float()
