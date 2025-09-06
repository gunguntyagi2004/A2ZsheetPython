# def majorityElement(arr):
#     n=len(arr)
#     ans=[]
#     for i in range(n):
#         count=1
#         for j in range(n):
#             if(arr[i]==arr[j]):
#                 count+=1
#         if (count >(n/3) and arr[i] not in ans):
#            ans.append(arr[i])
#     return ans


# def majorityElement(arr):
#     n=len(arr)
#     ans=[]
#     freqmap={}

#     for i in  range(n):
#         if arr[i] in freqmap:
#             freqmap[arr[i]]+=1
#         else:
#             freqmap[arr[i]]=1
#         if (freqmap[arr[i]]>(n/3) and arr[i] not in ans):
#             ans.append(arr[i])
#     return ans



def majorityElement(arr):
    n=len(arr)
    count1=0
    count2=0
    max1=0
    max2=0

    for i in range(n):
        if arr[i]==max1:
            count1 +=1
        elif arr[i]==max2:
            count2 +=1
        elif count1==0:
            max1=arr[i]
            count1=1
        elif  count2==0:
            max2=arr[i]
            count2=1
        else:
            count1-=1
            count2-=1          
    
    count1=0
    count2=0
    for i in range(n):
        if arr[i]==max1:
          count1 +=1
        elif arr[i]==max2:
         count2 +=1
    res=[]
    if count1>(n//3):
        res.append(max1)
    if count2>(n//3):
        res.append(max2) 
    return res      




arr=[1,1,1,1,2,3,2,2]
print(" list of majority element are",majorityElement(arr))