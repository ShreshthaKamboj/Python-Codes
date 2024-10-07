def max_product_of_two_integers():
    arr = [1,2,3,4,5]
    max_product = 0
    num1 = 0
    num2 = 0
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            max_product = max(max_product, arr[i]*arr[j])
            if max_product == arr[i]*arr[j]:
                num1 = arr[i]
                num2 = arr[j]
    print("Max Product of two integers in a array is ", max_product, num1, num2)
max_product_of_two_integers()
