import math

def example_function(name, radius):
    area = math.pi * radius ** 2
    return "The area of {} is {}".format(name, area)

print(example_function('Bobs_pond', 55))