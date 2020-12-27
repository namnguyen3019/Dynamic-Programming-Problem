
def fib(n):
    table = [0]*(n+1)
    # Base case
    table[0] = 0
    table[1] = 1

    for i in range(n):
        table[i+1] = table[i+1] + table[i]
        if i+2 < n:
            table[i+2] = table[i+2] + table[i]
    
    return table[-1]

# FIBONACCI: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34   
print(fib(5))
print(fib(8))
print(fib(10))