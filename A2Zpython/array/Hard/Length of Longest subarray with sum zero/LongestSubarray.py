# def longestSubarray(arr):
#     n=len(arr)
#     maxlen=0
#     for i in range (n):
#       sum=0
#       for j in range(i,n):
#          sum+=arr[j]
#          if sum==0:
#             length=(j-i)+1
#             maxlen=max(maxlen,length)

#     return maxlen        




def longestSubarray(arr):
    prefixSum={}
    sum=0
    maxlen=0

    for i ,num in enumerate(arr):
          sum+=num
          if sum==0:
               maxlen=i+1
          if sum in prefixSum:
               maxlen=max(maxlen,i-prefixSum[sum]) 
          else:
               prefixSum[sum]=i

    return maxlen                   



    










arr=[6, -2, 2, -8, 1, 7, 4, -10]
print("longest length of subarray",longestSubarray(arr))