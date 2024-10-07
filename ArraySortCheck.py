def Check_Sorted():
    arr = [1,2,3,4,5,6,7]
    bool = True
    for i in range(0, len(arr)-1):
        if arr[i]>arr[i+1]:
            bool = False
    print(bool)
Check_Sorted()
