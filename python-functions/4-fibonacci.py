def fibonacci_sequence(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    
    fib_numbers = [0, 1]
    while len(fib_numbers) < n:
        next_number = fib_numbers[-1] + fib_numbers[-2]
        fib_numbers.append(next_number)
    
    return fib_numbers

