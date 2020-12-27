'''
    Given a target number and a list of number
    Return the best way (the least number) to generate target sum
    Or return False if cannot generate target sum

'''

def bestSum(target, numbers):

    table = [None for i in range(target+1)]

    table[0] = []

    for i in range(target):
        for num in numbers:
            if i + num <= target:
                if table[i] is not None:
                    newWay = table[i] + [num]
                    if table[i+num] is None or len(newWay) < len(table[i+num]):
                        table[i+num] = newWay
    
    return table[target]

print(bestSum(7, [2,3,4]))
print(bestSum(9, [1, 2, 3, 4]))
print(bestSum(300, [7, 14]))

# m = target
# n = the length of number list

# Brute Force
# Time Complexity: O(n^m*m)
# Space Complexity  O(m^2)

# Tabulation
# Time Complexity: O(n*m^2)
# Space Complexity: O(m^2)