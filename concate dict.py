def check(d, key):
    if key in d:
        print("Key exists in the dictionary.")
    else:
        print("Key does not exist in the dictionary.")
dict1 = {}
n1 = int(input("Enter number of elements in 1st dictionary: "))
for i in range(n1):
    key = input("Enter key: ")
    value = input("Enter value: ")
    dict1[key] = value
dict2 = {}
n2 = int(input("\nEnter number of elements in 2nd dictionary: "))
for i in range(n2):
    key = input("Enter key: ")
    value = input("Enter value: ")
    dict2[key] = value
new_dict = dict1.copy()
new_dict.update(dict2)
print("\nConcatenated Dictionary:")
print(new_dict)
search_key = input("\nEnter key to search: ")
check(new_dict, search_key)
