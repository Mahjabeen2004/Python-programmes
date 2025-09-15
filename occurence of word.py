s=input("enter the word:")
v=s.split()
lists=[]
count=1
for i in v:
    lists.append(i)
    if i in lists:
        print(count(v))
