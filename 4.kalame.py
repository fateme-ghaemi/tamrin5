a1=[]
kalame=(list(input('kalame ra vared konid:')))
vowel=['a','e','u','i','o']
for i in kalame:
    if i in vowel:
        a1.append('?')
    else:
        a1.append(i)
a=''.join(a1)
print(a)


