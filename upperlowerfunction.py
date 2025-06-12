def count(s):
    u=0
    l=0
    for i in s:
        if i.isupper():
            u+=1
        elif i.islower():
            l+=1
    return u,l
si=input()
print(count(si))