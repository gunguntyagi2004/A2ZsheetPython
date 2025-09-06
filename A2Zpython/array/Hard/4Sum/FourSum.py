
# def fourSum(arr,K):
#     ans=set()
#     n=len(arr)
#     for i in range(n):
#         for j in range(i+1,n):
#             for k in range(j+1,n):
#                 for l in range(k+1,n):
#                    if(arr[i]+arr[j]+arr[k]+arr[l]==K):
#                      triplet=tuple(sorted([arr[i],arr[j],arr[k],arr[l]]))
#                      ans.add(triplet)

#     return [list(t) for t in ans]



# def fourSum(arr,K):
#     ans=set()
#     n=len(arr)
#     for i in range(n):
#         for j in range(i+1,n):
#             hashset=set()
#             for k in range(j+1,n):
#                 sum=arr[i]+arr[j]+arr[k]
#                 fourth=K-sum
#                 if fourth in hashset:
#                      triplet=tuple(sorted([arr[i],arr[j],arr[k],fourth]))
#                      ans.add(triplet)
#                 else:
#                     hashset.add(arr[k]);     
#     return [list(t) for t in ans]


def fourSum(arr,K):
    
    arr.sort()
    ans=set()
    n=len(arr)
    for i in range (n):
        if (i!=0 and arr[i]==arr[i-1]): continue
        for j in range(i+1,n):
            if (j >i+1 and arr[j]==arr[j-1]): continue
            k=j+1
            l=n-1
            while(k<l):
                sum=arr[i]+arr[j]+arr[k]+arr[l]
                if(sum<K):
                    k+=1
                elif(sum>K):
                       l-=1
                else:
                    triplet=tuple(sorted([arr[i],arr[j],arr[k],arr[l]]))
                    ans.add(triplet)      
                    k+=1
                    l-=1
                    while(k < l and arr[k]==arr[k-1]):k+=1
                    while(k<l and arr[l]==arr[l+1]): l-=1   

    return [list(t) for t in ans]











arr=[1,0,-1,0,-2,2]
K=0
print("all quadraple is",fourSum(arr,K))