a={}
b={}
s=input()
t=input()
for i in s:
    if i not in a:
        a[i]=1
    else:
        a[i]+=1

for i in t:
    if i not in b:
        b[i]=1
    else:
        b[i]+=1
if a==b:
    print("True")
else:
    print("False")