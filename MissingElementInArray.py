def missing_element():
    arr = [1,2,3,5]
    sum = 0
    for i in arr:
        sum += i
    n = max(arr)
    originalsum = int(n*(n+1)/2)
    print("Missing Element is", originalsum - sum)
missing_element()