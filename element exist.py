tup=('1','dia','20.2','ria')
n=raw_input("Enter value to check: ")
for i in tup:
   if(i==n):
      print "Element exist"
      break
else:
   print "Element not exist"
