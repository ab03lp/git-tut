a={}
c={}
s=input()
t=input()
for i in s:
    if i not in a:
        a[i]=1
    else:
        a[i]+=1

for i in t:
    if i not in c:
        c[i]=1
    else:
        c[i]+=1             #blah13
if a==c:
    print("True")
else:
    print("False")