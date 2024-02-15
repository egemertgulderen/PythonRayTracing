from vec3 import vec3 as point3
import vec3
import math
from hittable import hittable as h

from interval import interval


class sphere(h):
    def __init__(self, center, radius, material):
        self.center = center
        self.radius = radius
        self.material = material

    def hit(self, ray, ray_t, record):
        # length of ray from center to point
        oc = ray.get_origin() - self.center
        # Values of quadratic equations ax^2 + bx + c
        # Simplified values for equations according to (-b -+ sqrt(discriminant)) / a
        # b = 2h example

        a = ray.get_direction().length_squared()
        half_b = vec3.dot(oc, ray.get_direction())
        c = oc.length_squared() - self.radius * self.radius

        discriminant = half_b * half_b - a * c
        if discriminant < 0:
            return False

        sqrtd = math.sqrt(discriminant)

        # Find the nearest root between t_min and t_max
        root = (-half_b - sqrtd) / a
        if not (ray_t.surrounds(root)):
            root = (-half_b + sqrtd) / a
            if not (ray_t.surrounds(root)):
                return False

        record.t = root
        record.p = ray.at(record.t)
        outward_normal = (record.p - self.center) / self.radius
        record.set_face_normal(ray, outward_normal)
        record.mat = self.material

        return True
