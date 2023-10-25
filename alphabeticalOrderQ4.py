sen=input("Enter the word:")
sen=sen.upper()
sort=sorted(sen)#sorted list
merg="".join(sort)#list to string
rev=merg[::-1]#rversing the string
print("Alphabetical Order Normal : ",merg)
print("Alphabetical Order Normal Revrese : ",rev)
