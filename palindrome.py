
def palindrome(str): 
    for i in range(0, len(str)//2):  
        if str[i] != str[len(str)-i-1]: 
            return False
    return True
  

s = input()
ans = palindrome(s) 
  
if (ans): 
    print("YES") 
else: 
    print("NO")
