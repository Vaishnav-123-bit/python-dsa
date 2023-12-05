#find min elment and store at equivalent positon
#login in each pass min elment selected and placed at i th location

def selecitonSort(arr):
    for i in range(0,len(arr)-1):  #for passes  creating min reference
        min=arr[i];
        pos=i
        for j in range(i+1,len(arr)):       #search smallest 
            if(arr[j]<min):
                min=arr[j]
                pos=j;
        arr[i],arr[pos]=arr[pos],arr[i]

    return arr
        
arr=[3,1,2,4,6,7]
print(arr,"Before")
print(selecitonSort(arr),"After")
