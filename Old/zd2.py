a=int(input())
b=int(input())
c=int(input())
if c<a and c<b and b<a:
    print(c,b,a)
elif a<c and a<b and b<c:
    print(a,b,c)
elif a<b and a<c and c<b:
    print(a,c,b) 
else:
    b<a and b<c and a<c
    print(b,c,a)