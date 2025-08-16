#   Brute Force

import math;
# def maxsubarray(arr):
#     st=0
#     end=0
#     ms=-math.inf
#     for i in range(len(arr)):
#         cs=0
#         for j in range(i,len(arr)):
#              cs+=arr[j]
#              if cs>ms:
#                 ms=cs
#                 st=i
#                 end=j
#     for i in range(st,end+1):
#             print(arr[i])        
#     return ms


# Optimization

def maxsubarray(arr):
    cs=0
    ms=-math.inf
    st=0
    ansst=0
    ansend=0
    for i in range(len(arr)):
        cs+=arr[i]
        if(cs>ms):
            ms=cs
            ansst=st
            ansend=i
        if cs<0:
            cs=0
            st=i+1
    for i in range(ansst,ansend+1):
        print(arr[i])
    return ms


arr= [-2,1,-3,4,-1,2,1,-5,4] 
print("maximum sum is:-",maxsubarray(arr))


