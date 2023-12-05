# insertion sort unsorted element compared to sored and pproperly stroed element


#lgic : -> divide into 2 parts unsorted in each pass an element from unsorted is inserted at at correct loaction in sorted part
#


def insertionSort(arr):
    for i in range (0,len(arr)-1):
        element=arr[i+1]
        j=i+1;
        while j>0 and arr[j-1]>element:
            arr[j]=arr[j-1]
            j=j-1
        arr[j]=element
    return arr

arr=[3,1,2,4,6,7]
print(arr,"Before")
print(insertionSort(arr),"After")
            
            