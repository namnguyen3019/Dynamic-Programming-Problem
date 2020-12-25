'''
    Using memoization to solve fibonacci problem
'''

# Time complexity: O(n)
# Space complexity: O(n)
def fib(n, memo={}):
    if n in memo: return memo[n]
    if n < 0: return
    if n <=2 : return 1

    memo[n] = fib(n-1) + fib(n-2)

    return memo[n]

print(fib(5))
print(fib(6))
print(fib(50))