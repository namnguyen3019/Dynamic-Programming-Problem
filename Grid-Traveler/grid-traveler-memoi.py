
'''
    Problem description:
    Given 2D grid. You can only move down or right each time.
    How many ways to travel from top-left corner to bottom-right corner

'''
# Time complexity: O(2^(m+n))
# Space complexity: O(n+m)
def gridTraveler(m,n, memo={}):         # m: number of column, n: number of row
    if (m,n) in memo: return memo[(m,n)]
    if m < 1 or n < 1: return           # Check valid grid
    if m == 1 or n == 1: return 1

    memo[(m,n)] = gridTraveler(m-1, n, memo) + gridTraveler(m, n-1, memo)
    memo[(n,m)] = memo[(m,n)]

    return memo[(m,n)]

print(gridTraveler(2,3))    #3
print(gridTraveler(3,3))    #6
print(gridTraveler(20,20))  #