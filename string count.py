def characters(s):
    char_count = {}
    for char in s:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count
string = raw_input("Enter a string: ")
result = count_characters(string)
print("\nString: " + string)
print("Character occurrences: " + str(result))
