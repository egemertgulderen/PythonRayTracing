

class interval:
    def __init__(self, min=float('inf'), max=-float('inf')):
        self.min = min
        self.max = max

    def contains(self, x):
        return self.min <= x <= self.max

    def surrounds(self, x):
        return self.min < x < self.max

    def clamp(self, x):
        if x < self.min:
            return self.min
        if x > self.max:
            return self.max

        return x

    def get_max(self):
        return self.max

    def get_min(self):
        return self.min


empty_interval = interval(float('inf'), float('-inf'))
universe_interval = interval(float('-inf'), float('inf'))
