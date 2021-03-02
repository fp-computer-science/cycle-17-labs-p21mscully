# Author MRS 3/2/21

def factorial(number):
    if umber == 0:
        return 1
    else:
        recurse = factorial(number - 1)
        result = number * recurse
        return result


print(factorial(3))