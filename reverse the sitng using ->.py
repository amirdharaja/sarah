n=int(input())
l=list(map(int,input().split()))
l=l[::-1]
for i in range(0,len(l)-1):
    print(str(l[i])+'->',end='')
print(l[len(l)-1],end='')
