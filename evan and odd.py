num=int(input("entre your number"))
if(num%2==0):
    print("it is even number")
else:
    print ("it is an odd number")
#find the gratest value 
a=int(input("entre your firstnumber"))
b=int(input("entre your second number"))
c=int(input("entre your third number"))
if(a>b and a>c):
    print("this is the gratest number",a)
elif(b>a and b>c):
    print("the bigesst number",b)
else:
    print("the gratest number",c)
