#copyright to AMIRDHARAJAN


def palindrome(n):
    n1=n
    rev=0
    while n>0:
        rev=rev*10+n%10
        n=n//10
    print(rev,n1)
    if n1==rev:
        print("yes")
    else:
        print("no")
     
n=int(input(""))
palindrome(n)

  
