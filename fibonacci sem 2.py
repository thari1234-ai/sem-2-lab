#terms
n =int(input("Enter the number of terms: "))
a, b = 0, 1
print("Fibonacci sequence:")
for _ in range(n):
    print(a, end=" ")
    a, b = b, a + b
#snother method count
num=int(input())
n1=0
n2=1
count=0
if num==1:
    print("1")
elif num>0:
    while num-1>count:
        n3=n1+n2
        n1=n2
        n2=n3
        count+=1
print(n1)

