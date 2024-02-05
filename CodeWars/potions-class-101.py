from math import ceil

class Potion:
    def __init__(self, color, volume):
        self.color = color
        self.volume = volume

    def mix(self, other):
        new_color = list(self.color)
        new_volume = other.volume + self.volume

        for i in range(len(self.color)):
            # ((V1 x C1) + (V2 x C2)) / (V1 + V2)
            new_color[i] = ceil((self.volume * self.color[i] + other.volume * other.color[i]) / new_volume)


        new_color = tuple(new_color)
        return Potion(new_color, new_volume)
