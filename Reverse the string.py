def reverse(s,n=0):
    if(n==len(s)-1):
        print(s[n],end='')
    else:
        reverse(s,n+1)
        print(s[n],end="")
s=input()
reverse(s)
