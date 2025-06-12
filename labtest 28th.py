def hanoi(n,start,temp,end):
    if n==1:
        print("Move disk 1 from rod",start,"to rod",end)
        return
    hanoi(n-1,start,end,temp)
    print("Move disk",n,"from rod",start,"to rod",end)
    hanoi(n-1,temp,start,end)

n=int(input("Enter num:"))
hanoi(n,'A','B','C')