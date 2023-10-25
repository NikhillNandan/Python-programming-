num=int(input("Eenter a number : "))
r=num
while r!=1 and r!=4:
    s=0
    t=r
    while t!=0:
        d=t%10
        s+=d**2
        t=t//10
    r=s
if r==1:
    print("Given number is a HAPPY NUMBER:")
else:
    print("Given number is not a HAPPY NUMBER:")
