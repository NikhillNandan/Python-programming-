s = input("Enter the string:")
s=s.lower()
r=[]
print("Repeated Letters are : "); 
for i in range(0, len(s)):  
    c = 1
    for j in range(i+1, len(s)):
        if(s[i]==s[j] and s[i] != ' '):  
            c+=1
            s = s[:j] + '0' + s[j+1:]  
    if(c > 1 and s[i] != '0'):
        r.append(s[i])
        print(s[i],c)
print("Number of repeated characters :", len(r)," Repeated Letter is :",r)
