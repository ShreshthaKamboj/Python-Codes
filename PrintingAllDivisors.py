def PrintAllDivisors():
    num = 24
    for i in range(1, num+1):
        print(i, "is a Diviosor" if num % i == 0 else "Not a Divisor")
PrintAllDivisors()