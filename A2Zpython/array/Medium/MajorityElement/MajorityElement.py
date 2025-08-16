
#Brute Force

# def majority(arr):
#       n = len(arr)
#       for i in range(n):
#         count = 0
#         for j in range(i+1, n):
#             if arr[i] == arr[j]:
#                 count += 1
#         if count >= (n / 2):
#             return arr[i]
#       return None
            


def majority(arr):
     freq=1
     n=len(arr)
     ans=arr[0]
     for i in range(1,n):
          
          if(arr[i]==arr[i-1]):
               freq+=1
          else:
               ans=arr[i]
               freq=1
          if freq>=(n/2):
                return ans
     return None       
                   




arr=[1,2,2,2,2,1]
print("majority elment is :-",majority(arr))