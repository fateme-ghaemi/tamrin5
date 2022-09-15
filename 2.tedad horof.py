from ast import In
count3=0
count2=0
count1=0
count=0
harf=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','w','x','y','z']
space=[' ','\n']
comma=[',','.']
jomle=(input('jole ra vared konid:'))
for i in jomle:
    if i in harf:
        count+=1
for i in jomle:
    if i in space:
        count1+=1
for i in jomle:
    if i in comma:
        count2+=1
print('tedad harf :',count)
print('tedad char:',len(jomle))
print('tedad space:',count1) 
print('tedad comma & dot:',count2)
   


print('tedad kalame:',(jomle.split))

