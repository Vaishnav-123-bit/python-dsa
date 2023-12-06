def Merger(a,start,mid,end):
    i=start
    j=mid+1
    temp=[0]
    temp=temp*len(a)
    tindex=start
    while i<=mid and j<=end:
        if a[i]<a[j]:
            temp[tindex]=a[i]
            i+=1
            tindex+=1
        else:
            temp[tindex]=a[j]
            j+=1
            tindex+=1
    while i<=mid:
        temp[tindex]=a[i]
        i+=1
        tindex+=1
    while j<=end:
        temp[tindex]=a[j]
        j+=1
        tindex+=1
    for i in range(start,end+1):
        a[i]=temp[i]

def MergeSort(a,start,end):
    if start<end:
        mid=(start+end)//2
        MergeSort(a,start,mid)
        MergeSort(a,mid+1,end)
        Merger(a,start,mid,end)
    return a
arr=[3,1,2,4,6,7]
print(arr,"Before")
print(MergeSort(arr,0,len(arr)-1),"After")