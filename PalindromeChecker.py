def PalindromeChecker():
    num = 1551
    original = num      # Store the copy of the original number
    count = 0           # Initialize the count as 0
    reversenumber = 0   # Store the reverse number
    while num > 0:  # Loop until number is less than 0
        b = num % 10
        reversenumber = (reversenumber * 10) + b # Reverse number logic
        count = count + 1
        num = num // 10
    print("The total number of digits are: ",count)
    print("The reverse of the number is: ",reversenumber)
    print("Palindrome" if reversenumber==original else "Not Palindrome")
PalindromeChecker()