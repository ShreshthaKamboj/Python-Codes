def ArmstrongChecker():
    num = 372
    original = num      # Store a copy of original number
    sum = 0             # Initialize the sum as 0
    while num > 0:      # Loop until number is less than 0
        a = num % 10
        sum += a**3     # armstrong number logic
        num = num // 10
    print("Armstrong Number" if original==sum else "Not Armstrong")
ArmstrongChecker()
