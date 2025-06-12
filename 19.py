r,c=map(int,input().split())
A=[list(map(int,input().split())) for _ in range(r)]
B=[list(map(int,input().split())) for _ in range(r)]
for i in range(r):
    print(*[A[i][j]*B[i][j] for j in range(c)])