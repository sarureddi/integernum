num,num1=map(int,input().split())
l1=list(map(int,input().split()))
c1=int(input())
s1=0
for i in range(len(l1)):
    if i!=num1:
        s1=s1+l1[i]
if (s1//2)>=c1:
    print("Bon Appetit")
else:
    print((c1-(s1//2)))
