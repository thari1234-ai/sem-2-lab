choice=input()
if choice =="c":
    c=float(input())
    f=(c*9/5)+32
    print(round(f,2))
elif choice == "f":
    f=float(input())
    c=(f-32)*5/9
    print(round(c,2))
else:
    print("invalid")