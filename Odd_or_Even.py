n = int(input())
if n == 0:
    print("Zero")
elif n % 2 == 0 and n >= 0:
    print("Even")
elif n % 2 != 0 and n >= 0:
    print("Odd")
else:
    print("Invalid")