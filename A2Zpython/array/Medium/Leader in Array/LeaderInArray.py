# def leaderInArray(arr):
#     ans=[]
#     for i in range(len(arr)):

#         leader =True
#         for j in range(i+1,len(arr)):
#             if(arr[i]<arr[j]):
#                 leader=False
#                 break
#         if (leader):
#             ans.append(arr[i])
#     return ans

def leaderInArray(arr):
    ans=[]
    n=len(arr)
    max_element=arr[-1]
    ans.append(max_element)
    for i in range(n-2,-1,-1):
      
       if(arr[i]>max_element):
           max_element=arr[i]
           ans.append(max_element)
    return ans[::-1]



arr=[15,18,5,3,6,2]
print("leaders are:-",leaderInArray(arr))