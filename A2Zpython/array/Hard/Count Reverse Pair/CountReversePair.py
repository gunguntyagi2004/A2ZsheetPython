
# def pairs(arr,n):
#     count=0
#     for i in range(n):
#         for j in range(i+1,n):
#             if(arr[i]>2*arr[j]):
#                 count+=1

#     return count

def merge(arr,st,mid,end):
     temp=[]
     left=st
     right=mid+1
    
     while(left<=mid and right<=end):
          if(arr[left]<=arr[right]):
               temp.append(arr[left])
               left+=1
          else:
             temp.append(arr[right]) 
             right+=1
     while(left<=mid):
          temp.append(arr[left])
          left+=1
     while(right<=end):
          temp.append(arr[right])
          right+=1   
     for i in range(st, end + 1):
        arr[i] = temp[i - st]       








def countPairs(arr,st,mid,end):
    right=mid+1
    count=0
    for i in range(st,mid+1):
        while(right<=end and arr[i]>2*arr[right]):
                 right+=1
        count+=(right-(mid+1))
    return count





def mergeSort(arr,st,end):
    count=0
    if st>=end: return count
    mid=(end+st)//2
    count+=mergeSort(arr,st,mid)
    count+=mergeSort(arr,mid+1,end)
    count+=countPairs(arr,st,mid,end)
    merge(arr,st,mid,end)
    return count






def pairs(arr,n):
    return mergeSort(arr,0,n-1)




arr=[4, 1, 2, 3, 1]
n=5
print("count od all pairs are",pairs(arr,n))