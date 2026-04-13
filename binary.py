data = raw_input("enter 4 digit binary number by comma:")
numbers=data.split(",")
result=[]
for b in numbers:
   decimal=int (b,2)
   if decimal %5==0:
      result.append (b)
      print"output:"",".join(result)
