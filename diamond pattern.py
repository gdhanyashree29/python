n = int(input("ENTER n VALUE:"))
for i in range(n):
   for j in range(n-i-1):
         print " ",
   for k in range(2*i+1):
         print "*",
   print
for i in range(n-2,-1,-1):
   for j in range(n-i-1):
            print " ",
   for k in range(2*i+1):
            print "*",
   print
