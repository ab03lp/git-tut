P1=[1,2,3,4,5,6]
P2=[3,3,3,4,4,4,5,5,5]

p=len(P1)
q=len(P2)

r=set(P1)
s=set(P2)


if len(r)<=3:
    totala=p+0
elif len(r)>=6:
    totala=p+4

if len(s)<=3:
    totalb=q+0
elif len(s)>=6:
    totalb=q+4


if totala>totalb:
    print("P1 wins hehe")
else:
    print("P2 wins hehehe")
