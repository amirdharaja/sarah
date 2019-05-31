#by Amirdharajan

n,m=map(int ,input().split())#Which range you want to check the ODD numbers, Give value1 value2
for i in range(n+1,m):
    if i%2==0:
        print(i,end=" ")

