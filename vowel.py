s=input()
s1="AEIOUaeiou"
s2="!@#$%^&*()_"
if s in s1:
  print("Vowel")
elif s in s2:
  print("invalid")
else:
  print("Consonant")
