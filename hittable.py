import ray
from abc import ABC, abstractmethod
import vec3

import material


class hit_record:
    def __init__(self, p=vec3.vec3([0, 0, 0]), normal=vec3.vec3([0, 0, 0]), t=0.0, front_face=False, mat=None):
        self.p = p
        self.normal = normal
        self.t = t
        self.front_face = front_face
        if mat is None:
            # Replace DefaultMaterial with your default material class
            mat = material.DefaultMaterial(vec3.vec3([1.0, 1.0, 1.0]))

        self.mat = mat

    # Function for setting variables of Hit Records

    def update_record(self, new_p, new_normal, new_t, new_mat):
        self.p = new_p
        self.normal = new_normal
        self.t = new_t
        self.mat = new_mat

    def set_face_normal(self, ray, outward_normal):
        # Sets the hit record normal vector.
        # NOTE: the parameter `outward_normal` is assumed to have unit length.

        self.front_face = vec3.dot(ray.get_direction(), outward_normal) < 0
        self.normal = outward_normal if self.front_face else -outward_normal


class hittable(ABC):
    @abstractmethod
    def hit(self, ray, t_min, t_max, record):
        pass
