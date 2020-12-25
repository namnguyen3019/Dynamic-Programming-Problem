'''
    Given a target number and a list of number?
    Return True if we can generate the target number from the list. (use additional only)
    Can use any number in the list multiple times.

'''
# n is the target, m is the number in the list
# Time Complexity: O(n^m)
# Space Complexity: O(m): for the stack
def canSum(target, numbers):
    
    if target < 0: return False
    if target == 0: return True

    for num in numbers:
        remainder = target - num
        if canSum(remainder, numbers):
            return True
    return False

print(canSum(7, [2,4]))
print(canSum(100, [1,2,4]))
print(canSum(300, [7, 14]))
