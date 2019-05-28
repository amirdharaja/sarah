try:
  N,K=map(int,input().split())
  list1=[]
  for i in range(1,N+1):
    list1.append(i)
  print(sum(list1[:K]))
except:
  print("Give valid input")
