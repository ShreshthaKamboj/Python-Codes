def reverse_string(s):
    stack = []
    for char in s:
        stack.append(char)
    result = ''.join([stack.pop() for _ in range(len(stack))])
    return result
print(reverse_string("Hello"))
