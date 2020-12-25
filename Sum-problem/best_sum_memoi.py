'''
    Given a target number and a list of number
    Return the best way (the least number) to generate target sum
    Or return False if cannot generate target sum

'''

def bestSum(target, numbers, memo={}):
    # If already computed, return memo[target]
    if target in memo: return memo[target]
    if target < 0: return None

    if target == 0: return []

    shorestPath = None

    for num in numbers:
        remainder = target - num
        remainderResult = bestSum(remainder, numbers, memo)
        memo[target] = remainderResult
        if remainderResult is not None:
            # This is linear time
            path = remainderResult + [num]
            if shorestPath is None or len(shorestPath) > len(path):
                shorestPath = path
    
    return shorestPath

print(bestSum(7, [2,3,4]))
print(bestSum(9, [1, 2, 3, 4]))
print(bestSum(300, [7, 14]))

