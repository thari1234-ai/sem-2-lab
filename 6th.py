e=0
o=0
arr=[]
n=int(input())
for _ in range(n):
    arr.append(int(input()))
for i in arr:
    if i%2==0:
        e+=1
    else:
        o+=1
print("even",e)
print("odd",o)
               