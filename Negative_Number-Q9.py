n=[]
length=int(input("Enter the number fo elemnets:"))#size
for i in range(0,length):
    k=int(input())
    n.append(k)#store elements
c = 0
for i in n:
    if i < 0:#check for negative numbers
        c += 1
print("Number of negative numbers in the list:", c)
