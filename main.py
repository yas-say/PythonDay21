class Animal:
    def __init__(self):
        self.eyes = 2

    def move(self):
        print("I can walk")


class Fish(Animal):
    def __init__(self):
        super().__init__()
        self.tail = 1

    def swim(self):
        print("I can swim")

    def move(self):
        super().move()
        print("Underwater too")

nemo = Fish()
print(nemo.eyes)
nemo.move()
print(nemo.tail)
nemo.swim()
