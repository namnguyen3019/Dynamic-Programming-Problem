'''
    Fibonacci using simple recursive 
'''
# Time complexity: O(2^n)
# Space complexity: O(n)

def fib(n):
    if n < 0: return 
    if n <=2 :
        return 1
    return fib(n-1) + fib(n-2)

print(fib(5))
print(fib(6))
print(fib(50))