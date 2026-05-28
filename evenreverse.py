#WRITE A PYTHON PROGRAM WHICH WILL GENERATE even NUMBERS WITHIN N IN REVERSE ORDER
n=int(input("enter a number:"))
print("*"*50)
#logic
if(n<0):
    print("please enter a positive number")
else:
    if(n%2!=0):
        n-=1
    while(n>=0):
        print(n)
        n-=2
    else:
        print("this is while else part")
print("*"*50)
