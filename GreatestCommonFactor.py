def GCF():
    num1 = 6
    num2 = 12
    l1 = []     # List for storing divisors of number 1 
    l2 = []     # List for storing divisors of number 1
    N = num1 if num1>num2 else num2
    for i in range(1, N+1):
        if num1 % i == 0:
            l1.append(i)
        if num2 % i == 0:
            l2.append(i)
    common_divisors = list(set(l1) & set(l2))   # Intersection of l1 and l2
    gcf = max(common_divisors)  # Largest common divisor
    print("Greatest Common Factor of", num1, "and", num2,"is", gcf)
GCF()