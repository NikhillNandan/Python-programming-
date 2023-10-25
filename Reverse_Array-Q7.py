n=[]
length=int(input("Enter the number fo elemnets:"))#size
for i in range(0,length):
    k=int(input())#input elemenst
    n.append(k)#store elements in list
rev = n[::-1]#reversing the elements
print("Reverse Array elements =", rev)
    
