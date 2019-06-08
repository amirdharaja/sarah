n=int(input())
l=list(map(int,input().split()))
l1=[]
for i in range(len(l)):
    if i%2==0 and l[i]%2!=0 or i%2!=0 and l[i]%2==0:
        l1.append(l[i])
for i in l1:
    print(i,end=" ")

