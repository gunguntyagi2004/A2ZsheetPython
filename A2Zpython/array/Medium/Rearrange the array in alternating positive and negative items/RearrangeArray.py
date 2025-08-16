
# def rearrangeArray(arr):
#     pos=[]
#     neg=[]
#     n=len(arr)
#     for i in range(len(arr)):
#         if(arr[i]>=0):
#             pos.append(arr[i])
#         else:
#             neg.append(arr[i])
    
#     for i in range(n//2):
#         arr[2*i]=pos[i]
#         arr[2*i+1]=neg[i]

#     return arr

def rearrangeArray(arr):
    n=len(arr)
    pos=0
    neg=1
    ans=[0]*n
    for i in range(len(arr)):
        if(arr[i]>=0):
           ans[pos]=arr[i]
           pos+=2
        else:
            ans[neg]=arr[i]
            neg+=2
    
    
    return ans



arr=[1,2,-4,-5]
print("rearranged array is:-",rearrangeArray(arr))