def first_nonrepeat_char():
    string = "Aadidas"
    string = string.lower()
    dict = {}
    for char in string:
        if char not in dict:
            dict[char] = 1
        else:
            dict[char] += 1
    for i in dict:
        if dict[i] == 1:
            print("First non Repeating char is ", i)
            break
first_nonrepeat_char() 