def move_zeros_at_end(arr, n):
    j = -1
    for i in range(0, n):
        if arr[i]==0:
            j = i
            break
    if j==-1:
        return arr
    for i in range(j+1, n):
        if arr[i]!=0:
            temp = arr[j]
            arr[j] = arr[i]
            arr[i] = temp
            j += 1
    for i in range(0, n):
        print(arr[i], end = " ")
move_zeros_at_end([1,2,3,0,0,0,5,0,6], 9)