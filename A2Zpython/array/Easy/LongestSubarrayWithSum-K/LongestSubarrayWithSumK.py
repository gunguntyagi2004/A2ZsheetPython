# def longestSubarray(arr,K):
#     n=len(arr)
#     length=0
#     for i in range(n):
#         for j in range(i,n):
#             sum=0
#             for k in range(i,j+1):
#                 sum+=arr[k]
#             if(sum==K):
#                 length=max(length,j-i+1)    
#     return length


def longestSubarray(arr,K):
    n=len(arr)
    PS=[0]*n
    max_len=0
    PS[0]=arr[0]
    for i in range(1,n):
        PS[i]=PS[i-1]+arr[i]
    dic={}
    max_len=0
    for j in range(n):
        if(PS[j]==K):
            max_len=max(max_len,j+1)
        val=PS[j]-K
        if(val in dic):
            length=j-dic[val]
            max_len=max(max_len,length)
        if PS[j] not in dic:
            dic[PS[j]] = j
    return max_len


arr=[2,3,4,5,1,9]
# arr=[-1,1,1]
K=10
# K=1
print("length of longest subarray is:-",longestSubarray(arr,K))