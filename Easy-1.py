def last_length(s):
    # Remove leading and trailing spaces
    s = s.strip()

    # Find the last space in the modified string
    last_space_index = s.rfind(' ')

    # If there is no space, the entire string is the last word
    if last_space_index == -1:
        return len(s)

    # Otherwise, return the length of the last word
    return len(s[last_space_index + 1:])

str1 = input()
result = last_length(str1)
print(result)
