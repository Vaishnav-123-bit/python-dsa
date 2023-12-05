#complexity analysis

def fsum(n):
    sum=0;
    for i in range(1,n+1):            #n+1 times run    complexity=n+1  + n + constants (4) =O(2n+4)=O(2n)+O(4) =O(n)
        sum+=(i*i);                   #n time 
    
    print(sum)


# searching ->  2 / result is i(index of found) response is-1(not found)
# sorting-> 1 #

#sequiential search -> only search on usorted data/search until last found
#algo : 1.accept array(list)
#       2.till element not searched
#           2.1 if arr[i]==key
#       3.if arra over -1
# 
# #

 
#binary search   #