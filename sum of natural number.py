try:
  limit=int(input())
  total=0
  for i in range(1,limit+1):
    total += i
  print(total)
except:
  print("Enter INTEGER value only")
