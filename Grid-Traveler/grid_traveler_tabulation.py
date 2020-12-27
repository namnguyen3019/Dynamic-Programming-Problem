'''
    Problem description:
    Given 2D grid. You can only move down or right each time.
    How many ways to travel from top-left corner to bottom-right corner of the grid

'''

def gridTraveler(m, n):

    table = [[0 for col in range(m+1)] for row in range(n+1)]

    for j in range(1, m+1):
        table[1][j] = 1
    for i in range(1, n+1):
        table[i][1] = 1

    for i in range(2, n+1):
        for j in range(2, m+1):
            table[i][j] = table[i-1][j] + table[i][j-1]
    return table[n][m]

print(gridTraveler(3,2))
print(gridTraveler(3,3))
print(gridTraveler(3,4))