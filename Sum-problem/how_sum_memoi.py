'''
    Given a target number and a list of number?
    Return array of number if we can generate the target number from the list. (use additional only)
    Else return None
    Can use any number in the list multiple times.

'''

def howSum(target, numbers, memo={}):

    if target in memo: return memo[target]

    if target < 0: return None

    if target == 0: return []

    for num in numbers:
        remainder = target - num
        remainderResult = howSum(remainder, numbers, memo)
        if remainderResult is not None:
            memo[target] = remainderResult + [num]
            return memo[target]
    
    memo[target] = None
    # return memo[target]

print(howSum(7, [2,3,4]))
print(howSum(300, [7, 14]))