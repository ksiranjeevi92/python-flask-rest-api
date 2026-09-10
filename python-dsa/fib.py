def fib(n, memo=None):
    if memo is None:
        memo = {0: 0, 1:1}
    if n < 0:
        raise ValueError("Fibonacci is not defined for negative number")
    
    if n in memo:
        return memo[n]
    
    if n == 0 or n == 1:
        return n
    
    memo[n] = fib(n-1, memo) + fib(n-2, memo)

    return memo[n]

num = int(input("Please enter the number:"))

try:
 print(f"\n Fib of {num} is {fib(num)}")
except ValueError as e:
    print("Error rasied", e)
else:
    print("no error raised")
