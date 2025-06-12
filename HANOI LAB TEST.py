def hanoi(n,start,temp,end):
    if n==1:
        print("move disk from 1 ",start,"to rod",end)
        return
    hanoi(n-1,start,end,temp)
    print("move disk from",n,start,"to rod",end)
    hanoi(n-1,temp,start,end)
n=int(input())
hanoi(n,'A','B','C')