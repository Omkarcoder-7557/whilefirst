#WRITE A PYTHON PROGRAM WHICH WILL FIND mul OF FIRST N NATURAL NUMBERS
import sys
n=int(input("enter a number:"))
if(n<=0):
    print("please enter a positive integer")
    sys.exit()
else:
    i=1
    s=1
    while(i<=n):
        s=s*i
        i+=1
print("*"*50)
print("the mul first {} natural no is {}".format(n,s))
print("*"*50)