# def threeSum(arr):
#     n=len(arr)
    
#     ans=set()
#     for i in range(n):
#         for j in range(i+1,n):
#             for k in range(j+1,n):
#                 if(arr[i]+arr[j]+arr[k]==0):
#                     triplet=tuple(sorted([arr[i],arr[j],arr[k]]))
#                     ans.add(triplet) 
#     return [list(t) for t in ans]




# def threeSum(arr):
#     ans=set()
#     n=len(arr)
#     for i in range(n):
#         hashset=set()
#         for j in range(i+1,n):
#             third=0-(arr[i]+arr[j])
#             if third in hashset:
#                  triplet=tuple(sorted([arr[i],arr[j],third]))
#                  ans.add(triplet)
#             else:
#                 hashset.add(arr[j])
#     return [list(t) for t in ans]




def threeSum(arr):
    arr.sort()
    ans=set()
    n=len(arr)
    for i in range(n):
        if(i!=0 and arr[i]==arr[i-1]): continue
        j=i+1
        k=n-1
        while(j<k):
          sum=arr[i]+arr[j]+arr[k]
          if(sum>0):
             j+=1
          elif(sum<0):
             k-=1
          else:
             triplet=tuple(sorted([arr[i],arr[j],arr[k]]))
             ans.add(triplet)
             j+=1
             k-=1
             while(j<k and arr[j]==arr[j-1]): j+=1
             while(j<k and arr[k]==arr[k+1]): k-=1
    return ans






arr=[-1,0,1,2,-1,-4]
print("all triplets are",threeSum(arr))