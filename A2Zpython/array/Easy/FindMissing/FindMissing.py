# def find(arr,N):
#     for i in range(1, N + 1):
      
#         flag = 0
#         for j in range(len(arr)):
#             if arr[j] == i:
               
#                 flag = 1
#                 break

#         if flag == 0:
#             return i
#     return -1



def find(arr,N):
    sum1=(N*(N+1))/2
    sum2=0
    for i in range(len(arr)):
        sum2+=i
    return sum1-sum2



arr=[1,2,4,5]
N=5
print("missing number is:-",find(arr,N))