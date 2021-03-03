# Author MRS 3/3/21

wheels2 = 4
axels2 = 2
color2 = "red"

print(" The car has {0} wheels, {1} axels, and is {2}").format(wheels2, axels2, color2)

def build_car():
    wheels = 4
    axels = 2
    doors = 4
    color = "red"
    return("The car has {0} wheels, {1} axels, {2} doors, and is {3}".format(wheels, axels, doors, color))

print(build_car())
print(build_car())
print(build_car())