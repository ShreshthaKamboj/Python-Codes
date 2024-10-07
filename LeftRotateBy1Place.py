def left_rotation():
    arr = [1,2,3,4,5,6]
    temp = arr[0]
    for i in range(0, len(arr)-1):
        arr[i] = arr[i+1]
    arr[len(arr)-1] = temp
    for i in arr:
        print(i, end = " ")
left_rotation()