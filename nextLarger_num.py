#inp n=4 arr=[1,3,2,4]
#o/p = 3,4,4,-1


arr=[2,4,3,1]
for i in range(0,len(arr)):
    max=-1
    for j in range (i+1,len(arr)):
        if arr[j]>arr[i]:
            max=arr[j]
            break
    print(max,end=" ")
            
