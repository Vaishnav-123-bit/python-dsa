#works on unsorted data
# def sequentialSearch(array,key):
#     for i in range(len(array)):
#         if array[i]==key:
#             return i
#     return -1


# print(sequentialSearch([3,4,1,5],2))

#BINARY ->supposed to have sorted array/example of divide &conq/each pass reudyce problem size/faster/sorted only REQUIRIED

def bSearch(array,key,start,end):
    
    if start<=end:
        mid=(start+end)//2
        if key==array[mid]:
            return mid
        elif key<array[mid]:
            return bSearch(array,key,start,mid-1)
        else:
            return bSearch(array,key,mid+1,end)
    else:
        return -1 
array=[1,3,4,5,6,7]
print(bSearch(array,6,0,len(array)-1))