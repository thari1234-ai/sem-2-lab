n=int(input())
even=0
odd=0
arr=[]
for _ in range(n):
    arr.append(int(input()))
for i in arr:
    if i%2==0:
        even+=1
    else:
        odd+=1
print("even",even)
print("odd",odd)