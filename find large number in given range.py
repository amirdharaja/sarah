n=int(input())
l=list(map(int,input().split()))
l.sort()
l=l[::-1]
if sum(l)==0:
    print(0)
else:
    for i in l:
        print(i,end="")
