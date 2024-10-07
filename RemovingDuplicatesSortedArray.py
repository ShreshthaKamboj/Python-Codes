def remove_duplicates():
    arr = [1,1,2,3,4,5,5]
    i = 0
    size = 0
    for j in range(0, len(arr)-1):
        if arr[i]!=arr[j]:
            i += 1 
            arr[i] = arr[j]
            size += 1
    for i in range(0, size+1):
        print(arr[i], end = " ")
remove_duplicates()