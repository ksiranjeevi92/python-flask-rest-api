def fib(n):
    fib_list = [0,1]
    
    if n < 0:
        raise ValueError("Invalid number")
    
    for index in range(2,n+1):
        next_fib = fib_list[index - 1] + fib_list[index - 2]
        fib_list.append(next_fib)
    return fib_list[n]

print(f"\n Fib of {7} is {fib(7)}")