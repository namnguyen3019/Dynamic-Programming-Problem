'''
    Given a target number and a list of number?
    Return array of number if we can generate the target number from the list. (use additional only)
    Else return None
    Can use any number in the list multiple times.

'''

def howSum(target, numbers):
    if target < 0: return None

    if target == 0: return []

    for num in numbers:
        remainder = target - num
        remainderResult = howSum(remainder, numbers)
        if remainderResult is not None:
            return remainderResult + [num]

print(howSum(7, [2,3,4]))
print(howSum(300, [7, 14]))