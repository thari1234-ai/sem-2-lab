def fact(n):
    if n==0 or n==1:
        return 1
    else:
        return n*fact(n-1)
num=int(input())
if num<0:
    print("-")
if num==0 or num==1:
    print("1")
else:
    print("fact",fact(num))