'''
    Problem description:
    Given 2D grid. You can only move down or right each time.
    How many ways to travel from top-left corner to bottom-right corner

'''
def gridTraveler(m,n):      # m: number of column, n: number of row
    if m == 0 or n == 0: return 0
    if m == 1 or n == 1: return 1

    return gridTraveler(m-1, n) + gridTraveler(m, n-1)

print(gridTraveler(2,3))
print(gridTraveler(3,3))
print(gridTraveler(20,20)) # Can't compute