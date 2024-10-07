def single_element():
    arr = [1,2,1,2,3]
    xorr = 0
    for num in arr:
        xorr ^= num
    print(xorr)
single_element()