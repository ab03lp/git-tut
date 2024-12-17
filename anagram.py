# s=input()
# t=input()
# sorted(s)
# sorted(t)
# if len(s)==len(t):
#     print("anagram")
# else:
#     print("not anagram")


d={}
e={}
s=input()
t=input()
for i in s:
    if i not in d:
        d[i]=1
    else:
        d[i]+=1

for i in t:
    if i not in e:
        e[i]=1
    else:
        e[i]+=1
if d==e:
    print("True")
else:
    print("False")