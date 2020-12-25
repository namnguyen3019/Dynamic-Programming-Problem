'''
    Given a target number and a list of number?
    Return True if we can generate the target number from the list. (use additional only)
    Can use any number in the list multiple times.

'''
# Using memoization
# Time complexity:
# Space complexity:
def canSum(target, numbers, memo={}):
    
    if target in memo: return memo[target]
    if target < 0: return False
    if target == 0: return True

    for num in numbers:
        remainder = target - num
        if canSum(remainder, numbers):
            memo[target] = True
            return memo[target]
    
    memo[target] = False
    return False

print(canSum(7, [2,4]))
print(canSum(100, [1,2,4]))
print(canSum(300, [7, 14]))
