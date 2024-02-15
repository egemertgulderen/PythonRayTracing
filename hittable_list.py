from hittable import hittable as h
from hittable import hit_record as hit_rec
import vec3

# Importing interval
from interval import interval


class hittable_list(h):
    def __init__(self):
        self.objects = []

    def clear(self):
        self.objects.clear()

    def add(self, obj):
        self.objects.append(obj)

    def hit(self, ray, ray_t, record):
        temp_record = hit_rec()
        hit_anything = False
        closest_so_far = ray_t.get_max()
        for obj in self.objects:
            if (obj.hit(ray, interval(ray_t.get_min(), closest_so_far), temp_record)):
                hit_anything = True
                closest_so_far = temp_record.t
                record.update_record(
                    temp_record.p, temp_record.normal, temp_record.t, temp_record.mat)

        return hit_anything
