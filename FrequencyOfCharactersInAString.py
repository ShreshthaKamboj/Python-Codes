def freq_chars_in_string():
    string = "Hello World"
    string = string.lower()
    dict = {}
    for char in string:
        if char not in dict:
            dict[char] = 1
        else:
            dict[char] += 1
    print(dict)
freq_chars_in_string()