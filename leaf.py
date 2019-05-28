try:  
  year=int(input())
  if year%400==0 and year%4==0 or year%100==0:
    print("yes")
  else:
    print("no")
except:
  print("give valid input")
