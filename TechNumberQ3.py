n = int(input("Enter a number:"))
k = str(n)
a = k[:len(k)//2]#30
b = k[len(k)//2:]#25
c = int(a)+int(b)#55
d = c**2#3025
if d==n:
    print("Given number is a Tech number")
else:
    print("Given number is Not a Tech number")
