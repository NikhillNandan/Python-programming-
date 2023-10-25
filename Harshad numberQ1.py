n=int(input("Enter a number"))
t=n
s=0
while t!=0:
    d=t%10
    s+=d
    t=t//10
if n%s==0:
    print("Given number is Harshad Number")
else:
        print("Given number is not a Harshad Number")
