n=[]
length=int(input("ENter the number fo elemnets:"))
for i in range(0,length):
    k=int(input())
    n.append(k)
ncn=[]
for i in n:
    if i<2:
        continue
    c=0
    for j in range(2, i):
        if i%j==0:
            c+=1
            break
    if c==0:
        ncn.append(i)
print("Prime numbers in Array elements =", ncn)

