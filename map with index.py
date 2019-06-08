n=int(input())
l=list(map(int,input().split()))
l1=[]
len=len(l)
try:
    for i in range(0,len):
        if i==l[i]:
            l1.append(l[i])
    for i in l1:
        print(i,end=" ")
    if len(l1)!=0:
        print('-1')

except:
    print("")
