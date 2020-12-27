'''
    Given a target number and a list of number?
    Return True if we can generate the target number from the list. (use additional only)
    Can use any number in the list multiple times.

'''
# n is the target, m is the number in the list
# Time Complexity: O(n^m)
# Space Complexity: O(m): for the stack
def canSum(target, numbers):
    
    table = [False for i in range(target+1)]
    table[0] = True

    for i in range(target):
        for num in numbers:
            if i + num <= target:
                if table[i] is True:
                    table[i+num] = True
    
    return table[target]

print(canSum(7, [2,4]))     # False
print(canSum(100, [1,2,4])) # True
print(canSum(300, [7, 14])) # False
print(canSum(100, [5, 10, 15, 20])) # True
