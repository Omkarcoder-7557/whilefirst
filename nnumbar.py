#WRITE A PYTHON PROGRAM WHICH WILL GENERATE ONE TWO N NUMBERS WHERE N IS A POSITIVE INTEGER VALUE
print("*"*50)
n=int(input("enter a number:"))
print("*"*50)
#logic
if (n<=0):
    print("please enter a positive number")
else:
    i=0
    while(i<=n):
        print(i)
        i=i+1
    else:
        print("this is while else part")
print("*"*50)
print("program end")
print("*"*50)