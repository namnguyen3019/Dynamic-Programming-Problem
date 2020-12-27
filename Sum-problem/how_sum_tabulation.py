'''
    Given a target number and a list of number?
    Return array of number if we can generate the target number from the list. (use additional only)
    Else return None
    Can use any number in the list multiple times.

'''


def howSum(target, numbers):
    table = [None for i in range(target+1)]

    table[0] = []
    for i in range(target):

        for num in numbers:
            if i + num <= target:
                if table[i] is not None:
                    table[i+num] = table[i] + [num]
    

    return table[target]

print(howSum(7, [1,2,4]))
print(howSum(10, [2,3,5]))
print(howSum(300, [7, 14]))