def recur_factorial (n):
   if n==1:
     return n
   else:
     return n*recur_factorial(n-1)
# take input from the user
num=int(input("enter a number:"))
#check is the number is negative
if num<0:
  print("sorry , factorial does not exit for negative numbers")
elif num==0:
  print("defthe factorial if 0 is 1")
else:
  print("the factorial of",num,"is",recur_factorial(num))