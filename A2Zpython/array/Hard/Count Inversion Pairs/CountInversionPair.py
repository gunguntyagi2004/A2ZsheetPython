# def inversionPair(arr):
#       count=0
#       n=len(arr)
#       for i in range(n):
#             for j in range(i+1,n):
#                 if(arr[i]>arr[j]):
#                      count+=1  
#       return count 









def merge(arr,st,mid,end):
    left=st
    right=mid+1
    temp=[]
    count=0

    while(left<=mid and right<=end):
        if(arr[left]<=arr[right]):
            temp.append(arr[left])
            left+=1
        else:
            temp.append(arr[right])
            right+=1
            count+=(mid-left+1)
    
    while(left<=mid):
         temp.append(arr[left])
         left+=1
    
    while(right<=end):
        temp.append(arr[right])
        right+=1

    for i in range(st,end+1):
        arr[i]=temp[i-st]

    return count




def mergeSort(arr,st,end):
    n=len(arr)
    count=0
    if (st>=end): return count
    mid=(end+st)//2
    count+=mergeSort(arr,st,mid)
    count+=mergeSort(arr,mid+1,end)
    count+=merge(arr,st,mid,end)
    return count




def inversionPair(arr):
    n=len(arr)
    return mergeSort(arr,0,n-1)





arr=[5,4,3,2,1]

print("all inversion pair count",inversionPair(arr))