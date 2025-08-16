# def maximumSubarraySum(arr):
#     ms=0
#     for i in range (len(arr)):
#         cs=0
#         for j in range(i,len(arr)):
#            cs+=arr[j]
#            ms=max(ms,cs)
#     return ms       


import math;

def maximumSubarraySum(arr):
    cs=0
    
    ms=-math.inf
    for i  in range (len(arr)):
        
        
        cs+=arr[i]
       
        ms=max(ms,cs)
        
        if(cs<0):
            cs=0
            
    return ms




arr= [1,2,3,4,5]
print("maximum subarray sum is :-",maximumSubarraySum(arr))