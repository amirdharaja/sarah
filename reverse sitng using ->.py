n=int(input())
l=list(map(int,input().split()))
try:
    l=l[::-1]
    for i in range(0,len(l)-1):
        print(l[i],"->",end='')
    print(l[len(l)-1],end='')
except:
    print("")
