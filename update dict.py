dict1 = {"a" : 10,"b" : 50,"c" :60}
dict2 = {"c" : 20,"d" : 30}
print"dictionary 1:", dict1
print"dictionary 2:", dict2

merged_or = dict1.copy()
merged_or.update(dict2)
print"1. Using update():", merged_or

merged_update = dict1.copy()
merged_update.update(dict2)
print"2. Using update() function:", merged_update

merged_loop = dict1.copy()
for key, value in dict2.items():
    merged_loop[key] = value
print"3. Using for loop:", merged_loop
