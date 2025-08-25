number=[3,1,4,9,8,2,6]
print("length of the list number is:",len(number))
print("last element is:",number[-1])

number.reverse()
print("reversed list is:",number)

if 9 in number:
    print("yes,9 is in the list")
    
number.insert(7,7)
print(number)

