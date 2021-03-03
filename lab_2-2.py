# Author MRS 3/3/21

def build_vehicle(x, c ,v ,b):

    wheels = x
    axels = c
    doors = v
    color = b

    return (" The car has {0} wheels, {1} axels, {2} doors, and is {3}".format(wheels, axels, doors, color))

user1 = input( "How many wheels?")
user2 = input( "How many axels?")
user3 = input( "How many doors?")
user4 = input( "What color?")

build_vehicle(user1, user2, user3, user4)