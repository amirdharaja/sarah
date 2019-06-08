n=int(input())
l=list(map(int,input().split()))
l1=[]
length=len(l)
for i in range(length):
    if i%2==0 and l[i]%2!=0 or i%2!=0 and l[i]%2==0:
        l1.append(l[i])
print(l1)
