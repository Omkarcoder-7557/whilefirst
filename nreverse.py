#WRITE A PYTHON PROGRAM WHICH WILL GENERATE N TO 1 NUMBER WHERE N IS A POSITIVE INTEGER VALUE
n=int(input("enter a number:"))
print("*"*50)
#logic
if (n<=0):
    print("please enter a positive number")
else:
    while (n>=0):
        print(n)
        n-=1
    else:
        print("this is while else for related to while ")
print("*"*50)
print("program end")
print("*"*50)