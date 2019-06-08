n=int(input())
l=list(map(int,input().split()))
l1=[]
length=len(l)

for i in range(0,length):
    if i==l[i]:
        l1.append(l[i])
n=len(l1)
if n==0:
    print('-1')
else:
    for i in l1:
        print(i,end=" ")
