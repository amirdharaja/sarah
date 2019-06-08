while True:
    n=int(input())
    a={0:'zero',1:'one',2:'two',3:'three',4:'four',5:'five',6:'six',7:'seven',8:'eight',9:'nine',10:'ten'}
    b={1:'eleven',2:'twelve',3:'thirteen',4:'fourteen',5:'fifteen',6:'sixteen',7:'seventeen',8:'eighteen',9:'nineteen',20:'twenty'}
    c={1:'ten',2:'twenty',3:'thirty',4:'fourty',5:'fifty',6: 'sixty',7:'seventy',8:'eighty',9:'nighty',0:''}
    d=['hundred and']
    temp=0
    temp1=0

    if n<=10:
        if n==10:
            print(a[n])
        else:
            temp1=n%10
            print(a[temp1])
            
    elif n>10 and n<20:
        temp=int(n/10)
        temp1=n%10
        print(b[temp1])
    
    elif n>=20 and n<=99:
        temp=int(n/10)
        temp1=n%10
        if temp1==0:
            print(c[temp])
        else:
            print(c[temp],a[temp1])
    elif n>=100 and n<=999:
        temp=int(n%100)
        temp0=n//100
        temp1=temp//10
        temp2=n%10
        print(a[temp0], d[0], c[temp1],a[temp2])
    else:
        print("Please enter the value upto 999")
