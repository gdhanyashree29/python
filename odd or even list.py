n=raw_input("Enter the elements in the list: ")
even = []
odd = []
x = n.split(',')
for i in x:
    num = int(i)
    if num % 2 == 0:
        even.append(num)
    else:
        odd.append(num)
print "Even numbers:", even
even.extend(odd)
print "Odd number:", even
