def check_anagram():
    str1 = "Listen"
    str2 = "Silent"
    str1 = str1.lower()
    str2 = str2.lower()
    if len(str1) != len(str2):
        print("Not Possible to Check for Anagram")
    elif sorted(str1) == sorted(str2):
        print("Yes the strings are a pair of anagram")
    else:
        print("Not a anagram")
check_anagram()