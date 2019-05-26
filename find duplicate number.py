n=int(input("Enter the size of list"))
list1=[]
try:
    for i in range(1,n+1):
        print("Enter the value for position",i)
        temp=int(input())
        list1.append(temp)
    temp=[]
    list3=[]
    for i in list1:
        if i not in temp:
            temp.append(i)
        else:
            list3.append(i)
    list3.sort()
    list3=set(list3)
    for i in list3:
        print(i, end=" ")
except:
    print("Wrong Entry\ncarefully enter the value")
