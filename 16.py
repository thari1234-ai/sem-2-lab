n=int(input())
first=(n//100)**3
second=((n//10)%10)**3
third=(n%10)**3
t=first+second+third
if n==t:
    print("armstrong")
else:
    print("no")