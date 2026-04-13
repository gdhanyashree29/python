def prime(n):
   if  n <= 1:
        return 0
   for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return 0
   return 1
num = int(input("Enter a number: "))
if prime(num):
    print("(Prime Number)")
else:
    print("(Not a Prime Number)")
