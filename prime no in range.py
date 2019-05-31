#by Amirdharajan

n,m=map(int ,input().split())#Which range you want to check, Give value1 value2
for i in range(n,m+1):
    if i>1:
        for j in range(2,i):# limits 2 to i times
            if i%j == 0:
                break
        else:
            print(i,end=' ')

