m1=int(input())
m2=int(input())
m3=int(input())
m4=int(input())
m5=int(input())
t=m1+m2+m3+m4+m5
per=t/5
print(per)
if per>=80:
    print("grade a")
elif per>-70:
    print("grade b")
elif per>=60:
    print("c")
elif per>=40:
    print("d")
else:
    print("e")