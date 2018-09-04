import random

class Man:

    def __init__(self):

        self.height = random.randint(160, 210)
        self.weight = random.randint(70, 130)

    def grow(self):

        self.height += (random.randint(1,4))

    def fatten(self):

        self.weight += (random.randint(2,4))

