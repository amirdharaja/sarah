#by Amirdharajan

while True:
    n=int (input())#Which no you want to check
    if n>1: # input i always greater then 1
        for i in range(2,n):# limits 2 to n times
            if n%i == 0:
                print("no")
                break
            else:
                print("yes")
                break
    else:
        print("no")
