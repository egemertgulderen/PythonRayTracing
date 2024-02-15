import vec3
from ray import ray
from vec3 import vec3 as point3
from abc import ABC, abstractmethod


class material(ABC):
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def scatter(self, ray_in, record, attenuation, scattered):
        pass


class Lambertian(material):
    def __init__(self, albedo: point3):
        self.albedo = albedo

    def scatter(self, ray_in, record, attenuation, scattered):
        scatter_direction = record.normal + vec3.random_unit_vector()

        if scatter_direction.near_zero():
            scatter_direction = record.normal

        scattered.origin = record.p
        scattered.direction = scatter_direction
        attenuation[:] = self.albedo  # Update values in the existing list
        return True


class metal(material):
    def __init__(self, a: point3, f: float):
        self.albedo = a
        self.fuzz = min(f, 1.0)

    def scatter(self, ray_in, record, attenuation, scattered):
        reflected = vec3.reflect(vec3.unit_vector(
            ray_in.direction), record.normal)
        scattered.origin = record.p
        scattered.direction = reflected + self.fuzz * vec3.random_unit_vector()
        attenuation[:] = self.albedo
        return vec3.dot(scattered.direction, record.normal) > 0


# Problem at dielectric materials
class dielectric(material):
    def __init__(self, index_of_refraction: float):
        self.index_of_refraction = index_of_refraction

    def scatter(self, ray_in, record, attenuation, scattered):
        refraction_ratio = 1.0 / \
            self.index_of_refraction if record.front_face else self.index_of_refraction

        unit_direction = vec3.unit_vector(ray_in.get_direction())

        refracted = vec3.refract(
            unit_direction, record.normal, refraction_ratio)

        scattered.origin = record.p
        scattered.direction = refracted

        return True


class DefaultMaterial(Lambertian):
    def __init__(self, albedo: vec3):
        super().__init__(albedo)
