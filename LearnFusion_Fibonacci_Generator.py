def fibonacci(n):
    if n<=0:
        return "Input should be a positive integer."
    elif n==1 :
        return [0]
    elif n==2 :
        return [0,1]
    else:
        fib_sequence = [0,1]
        for i in range(2,n):
            next_number = fib_sequence[-1] + fib_sequence[-2]
            fib_sequence.append(next_number)
        return fib_sequence

n=10
print(fibonacci(n))
