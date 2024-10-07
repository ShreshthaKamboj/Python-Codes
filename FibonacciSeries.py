def fibonacci():
    first = 0       # First number of the series
    second =1       # Second number of the series
    n = 5           # Total elements in the Fibonacci series
    count = 2       # Counter starting after the first two numbers
    print(first, second, end=" ")
    while count<n:
        fib = first + second    # Fibonacci Logic
        first =second
        second = fib
        print(fib,end=" ")
        count += 1
fibonacci()