import math

from utility import random_float
from utility import random_of_float


class vec3:
    def __init__(self, e=[0, 0, 0]):
        self.e = e

    def x(self):
        return self.e[0]

    def y(self):
        return self.e[1]

    def z(self):
        return self.e[2]

    # Operator Functions
    def __neg__(self):
        return vec3([-self.x(), -self.y(), -self.z()])

    def __getitem__(self, i):
        return self.e[i]

    def __setitem__(self, i, value):
        self.e[i] = value

    def __iadd__(self, vec):
        self.e[0] += vec.x()
        self.e[1] += vec.y()
        self.e[2] += vec.z()
        return self

    def __imul__(self, vec):
        self.e[0] *= vec.x()
        self.e[1] *= vec.y()
        self.e[2] *= vec.z()
        return self

    def __itruediv__(self, vec):
        self.e[0] /= vec.x()
        self.e[1] /= vec.y()
        self.e[2] /= vec.z()
        return self

    def length_squared(self):
        return self.e[0]*self.e[0] + self.e[1]*self.e[1] + self.e[2]*self.e[2]

    def near_zero(self):
        s = 1e-8
        return abs(self.e[0]) < s and abs(self.e[1]) < s and abs(self.e[2]) < s

    def length(self):
        return math.sqrt(self.length_squared())

   # Utility Functions

    def __str__(self) -> str:
        return f'{self.x()} {self.y()} {self.z()}'

    def __add__(self, vec):
        return vec3([self.x() + vec.x(), self.y() + vec.y(), self.z() + vec.z()])

    def __sub__(self, vec):
        return vec3([self.x() - vec.x(), self.y() - vec.y(), self.z() - vec.z()])

    # vec can be int,float or another vector
    def __mul__(self, vec):
        if isinstance(vec, vec3):
            return vec3([self.x() * vec.x(), self.y() * vec.y(), self.z() * vec.z()])
        elif isinstance(vec, (int, float)):
            return vec3([self.x() * vec, self.y() * vec, self.z() * vec])
        else:
            raise TypeError(
                f"Unsupported type for multiplication: {type(vec)}")

    def __rmul__(self, vec):
        if isinstance(vec, (int, float)):
            return vec3([self.x() * vec, self.y() * vec, self.z() * vec])
        else:
            raise TypeError(
                f"Unsupported type for multiplication: {type(vec)}")

    def __truediv__(self, vec):
        if isinstance(vec, (int, float)):
            return self * (1/vec)
        else:
            raise TypeError(f"Unsupported type for division: {type(vec)}")

    @staticmethod
    def random():
        return vec3([random_float(), random_float(), random_float()])

    @staticmethod
    def random_of_float(min, max):
        return vec3([random_of_float(min, max), random_of_float(min, max), random_of_float(min, max)])


def dot(u, v):
    return (u.x() * v.x()) + (u.y() * v.y()) + (u.z() * v.z())


def cross(u, v):
    return vec3([(u.y() * v.z()) - (u.z() * v.y()),
                (u.z() * v.x()) - (u.x() * v.z()),
                (u.x() * v.y()) - (u.y() * v.x())])


def unit_vector(u):

    # NOTE: There is a problem with solving for 0 vectors

    return (u / u.length())


# Creating diffuse material

def random_in_unit_sphere():
    while (True):
        p = vec3.random_of_float(-1, 1)
        if p.length_squared() < 1:
            return p


def random_unit_vector():
    return unit_vector(random_in_unit_sphere())


def random_on_hemisphere(normal):
    on_unit_sphere = random_unit_vector()
    if dot(on_unit_sphere, normal) > 0.0:
        return on_unit_sphere
    else:
        return -on_unit_sphere


def reflect(v, n):
    return v - 2 * dot(v, n)*n


def refract(uv, n, etai_over_etat):
    cos_theta: float = min(dot(-uv, n), 1.0)
    r_out_perp = etai_over_etat * (uv + cos_theta * n)
    r_out_parallel = - \
        math.sqrt(math.fabs(1.0 - r_out_perp.length_squared())) * n

    return r_out_perp + r_out_parallel
