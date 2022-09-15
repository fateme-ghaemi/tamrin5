new=[]
for i in range(10):
    name=input('enter name:')
    a1=name.lower()
    a2=name[0].upper()
    a3=new.append(a2+name[1:])
print(new)