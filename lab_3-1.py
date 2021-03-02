# Author MRS 3/2/21

def r_max(lst):
    largest = 0
    for element in lst:
        if type(element) == list:
            val = r_max(element)
        else:
            val = element

        if val > largest:
            largest val
    
    return largest



print(r_max([1, 2, 3, [24, 31], 51]) == 31)