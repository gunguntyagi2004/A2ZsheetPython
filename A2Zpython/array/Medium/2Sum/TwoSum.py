# def twoSum(arr,target):
#      ans=[]
#      for i in range(len(arr)):
#           for j in range(i+1,len(arr)):
#                if(arr[i]+arr[j]==target):
#                     ans.append(i)
#                     ans.append(j)
#      return ans
     
    #Better Approach

# def twoSum(arr, target):
#     arr.sort()
#     st, end = 0, len(arr)-1
#     ans = []
#     while st < end:
#         s = arr[st] + arr[end]
#         if s == target:
#             ans.append((st, end))
#             break
#         elif s > target:
#             end -= 1
#         else:
#             st += 1
#     return ans

#optimize Approach

def twoSum(arr,target):
       ans = []
       dic = {}
       for i in range(len(arr)):
           val = target - arr[i]
           if val in dic:
             ans.append(dic[val])  
             ans.append(i)         
             break
           else:
             dic[arr[i]] = i       
       return ans    

arr = [1, 6, 2, 10, 3]
target = 7
print("pairs are:", twoSum(arr, target))

