s1 = input("Enter S1 : ")
s2 = input("Enter S2 : ")
n = int(input("Index :"))
r = ""
i = j=0
while i < len(s1) and j < len(s2):
    r = r+s1[i:i+n] + s2[j:j+n]
    i = i+n
    j = j+n
r += s1[i:] + s2[j:]
print(r)
