'''
    Fibonacci using simple recursive 
'''

def fib(n):
    if n < 0: return 
    if n <=2 :
        return 1
    return fib(n-1) + fib(n-2)

print(fib(5))
print(fib(6))
print(fib(50))