def bubbleSort(arr):
    for i in range(0,len(arr)-1):
        for j in range (0,len(arr)-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
            
        return arr


arr=[3,1,2,4,6,7]
print(arr,"Before")
print(bubbleSort(arr),"After")