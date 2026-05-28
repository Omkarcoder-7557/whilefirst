#WRITE A PYTHON PROGRAM WHICH WILL GENERATE MULTIPLICATION TABLE FOR A GIVEN POSITIVE INTEGER VALUE
n=int(input("enter a number:"))
print("*"*50)
if(n<=0):
    print("please enter a positive number")
else:
    i=1
    while (i<=10):
        print("({}*{})={}".format(n,i,n*i))
        i+=1
print("*"*50)