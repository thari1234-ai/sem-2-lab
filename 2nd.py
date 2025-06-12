m1=int(input())
m2=int(input())
m3=int(input())
m4=int(input())
m5=int(input())
t=m1+m2+m3+m4+m5
p=t/5
print("Percentage",p)
if p>=80:
    print("Grade A")
elif p>=70:
    print("Grade b")
elif p>=60:
    print("Gradec")
elif p>=40:
    print("D")
else:
    print("Grade e")