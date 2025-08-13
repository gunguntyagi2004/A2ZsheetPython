# def singleNumber(arr):
#     for i in range(len(arr)):
#         for j in range(1,len(arr)):
#          if arr[i]!=arr[j]:
#             return arr[i]
#     return -1


def singleNumber(arr):
    ans=0
    for i in range(len(arr)):
        ans=ans^arr[i]
    return ans    


arr=[4,1,2,2,1,4,5]
print("single number is:-",singleNumber(arr))