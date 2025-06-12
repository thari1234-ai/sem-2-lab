n=int(input())
d={}
for i in range(n):
    k=input()
    v=int(input())
    d[k]=v
t=sum(d.values())
print(t)