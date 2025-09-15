a=int(input("enter a number range:"))
numbers=[]
for i in range(a):
   i=int(input("enter the number:"))
   if i>100:
       numbers.append('over')
   else:
       numbers.append(i)
print(numbers)
