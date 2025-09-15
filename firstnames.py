names=['Anu','Meena','Rani','Anand']
list=[]
for i in names:
      count=0
      for j in i:
          j=j.lower()
          list.append(j)
for k in list:
    if k=='a':
     count+=1
print('count of a is',count)
