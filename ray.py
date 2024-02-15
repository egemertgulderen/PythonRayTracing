from vec3 import vec3


class ray():
    def __init__(self, origin=vec3([0, 0, 0]), direction=vec3([0, 0, 0])):
        self.origin = origin
        self.direction = direction

    def at(self, t):
        return (self.origin + t*self.direction)

    def get_origin(self):
        return (self.origin)

    def get_direction(self):
        return self.direction
