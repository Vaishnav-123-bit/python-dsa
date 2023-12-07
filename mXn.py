m=6
n=30
scount=Dcount=0
for i in range(1,n+1):
    if i%m==0:
        scount+=i;
        print(scount)
    else:
        Dcount+=i;
    
print(Dcount-scount)


