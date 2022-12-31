class Student:
    def __init__(self, name):
        self.name = name

movies = ['Matrix', 'Finding Nemo']

#everything is an object in python

class Garbage:
    def __init__(self):
        self.cars = []

    def __len__(self):
        return len(self.cars)


    def __getitem__(self, item):
        return self.cars[item]

    def __repr__(self):
        return f'<Garbage {self.cars}'

    def __str__(self):
        return f'Garbage with {len(self)} cars.'




ford = Garbage()
ford.cars.append('Fiesta')
ford.cars.append('Focus')

print(len(ford))
print(ford[0]) # = Garbage.__getitem__(ford, 0)
print(Garbage.__getitem__(ford, 1))

print(ford)
