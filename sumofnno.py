#WRITE A PYTHON PROGRAM WHICH WILL FIND SUM OF FIRST N NATURAL NUMBERS
n=int(input("enter a number:"))
if(n<0):
    print("please enter a positive integer")
else:
    i=0
    s=0
    while(i<=n):
        s=s+i
        i+=1
print("*"*50)
print("the sum first {} natural no is {}".format(n,s))
print("*"*50)