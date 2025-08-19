
 # brute force 0(n^2)

# def linearSearch(arr,K):
#     for i in range(len(arr)):
#         if(arr[i]==K):
#             return True
#     return False

# def longConsecutiveSeq(arr):
#     longest=1
#     for i in range(len(arr)):
#         x=arr[i]
#         cnt=1
        
#         while(linearSearch(arr,x+1)==True):
#             x=x+1
#             cnt+=1
#         longest=max(longest,cnt) 
#     return longest        






#better approach 0(nlogn)

# def longConsecutiveSeq(arr):
#     n=len(arr)

#     if n==0:
#         return 0
    
#     arr=sorted(arr)
#     prev=arr[0]
#     length=1
#     max_length=1

#     for i in range(1,n):
#         if(arr[i]==prev):
#             continue
#         elif arr[i]==(prev+1):
#             length+=1
#             prev=arr[i]
#         else:
#             length=1
#             prev=arr[i]
#         max_length=max(max_length,length)
#     return max_length
 

def longConsecutiveSeq(arr):
    s=set()
    n=len(arr)
    if n==0:
        return 0
    
    for i in range(n):
        s.add(arr[i])
    
    max_len=0
    for it in s:
        prev=it-1
        if prev not in s:
           length=1
           next=it+1
           while(next in s):
               length+=1
               next+=1
           max_len=max(max_len,length)
    return max_len    



arr=[100,102,4,101,3,2,1]
print("longest no of sequence is :-",longConsecutiveSeq(arr))