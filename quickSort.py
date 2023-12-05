def quickSort(a,start,end):
    i=start
    j=end
    pivot=start

    while i<j:
        while a[i]<a[pivot]:
            i+=1;
        while a[j]>a[pivot]:
            j-=1
        if i<j:
            a[i],a[j]=a[j],a[i]
    if i<end:
        return quickSort(a,i+1,end)
    elif start<j:
        return quickSort(a,start,j-1)
    return a

arr=[3,1,2,4,6,7]
print(arr,"Before")
print(quickSort(arr,0,len(arr)-1),"After")