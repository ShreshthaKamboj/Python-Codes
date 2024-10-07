def max_consecutive_ones():
    arr = [1, 0, 0, 0, 0, 1, 1, 1, 0, 1, 1, 1, 1]
    max_count = 0  # To store the maximum count of consecutive 1s
    freq = 0  # To count consecutive 1s
    
    for i in range(len(arr)):
        if arr[i] == 1:
            freq += 1  # Increment freq when you find a 1
            max_count = max(max_count, freq)  # Update max_count if freq is higher
        else:
            freq = 0  # Reset freq when you encounter a 0
    
    print(max_count)

max_consecutive_ones()