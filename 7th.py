u=0
l=0
s=input().strip()
for i in s:
    if i.isupper():
        u+=1
    elif i.islower():
        l+=1
print("upper",u)
print("lower",l)