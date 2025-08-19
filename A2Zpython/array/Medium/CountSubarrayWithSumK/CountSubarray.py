# def countSubarray(arr,K):
#     count=0
#     for i in range(len(arr)):
#         sum=0
#         for j in range(i,len(arr)):
#             sum+=arr[j]
#             if(sum==K):
#                 count+=1
#     return count


def countSubarray(arr,K):
    count=0
    n=len(arr)
    prefixsum=[0]*n
    prefixsum[0]=arr[0]
    for i in range(1,n):
        prefixsum[i]=arr[i]+prefixsum[i-1]
    dic={}
    for j in range(len(arr)):
        if(prefixsum[j]==K):
            count+=1
        val=prefixsum[j]-K
        if val in dic:
            count+=dic[val]
        dic[prefixsum[j]] = dic.get(prefixsum[j], 0) + 1
        
            
    return count        






arr=[3, 4, 7, 2, -3, 1, 4, 2]
k=7
print("count is:-",countSubarray(arr,k))