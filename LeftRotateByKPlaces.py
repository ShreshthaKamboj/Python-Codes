def left_rotate_k_places(arr, n, k):
    if n==0:
        print("Empty Array")
        return
    k = k % n
    if k>n:
        print("Not Possible")
        return
    arr[:] = arr[k:] + arr[:k]
    for i in range(0, n):
        print(arr[i], end = " ")
left_rotate_k_places([1,2,3,4,5,6,7], 7, 3)