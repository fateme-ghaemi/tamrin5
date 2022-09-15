new=[]

names=input('enter word:')
for i in names:
    new.append(i)
   
if new==new[::-1]:
     print('yes')
else:
     print('no')
print(new[::-1])