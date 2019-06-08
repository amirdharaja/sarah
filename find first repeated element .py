n=int(input())
l=list(map(int,input().split()))
l1,l2=[],[]
try:
    for i in l:
        if i in l1:
            l1.remove(l[i])
        else:
            l2.append(l[i])

    print(l2[0])
except:
    print("")
