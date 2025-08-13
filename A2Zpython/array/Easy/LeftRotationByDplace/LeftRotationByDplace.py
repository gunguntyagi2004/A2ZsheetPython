
      #Brute force

# def rotate(arr,d):
#     n=len(arr)
#     d=d%n
    
#     for i in range(d,n):
#         arr[i-d]=arr[i]
#     i=0
#     for j in range(n-d,n):
#         arr[j]=temp[i]
#         i+=1
#     return arr



def rotate(arr,d):
    n=len(arr)
    d=d%n
    reverse(arr,0,d-1)
    reverse(arr,d,n-1)
    reverse(arr,0,n-1)
    return arr

def reverse(arr,st,end):
    while(st<end):
        arr[st],arr[end]=arr[end],arr[st]
        st+=1
        end-=1



arr=[1,2,3,4,5,6,7]
d=2
temp=arr[:d]
print("before :-",arr)
print("Rotated array:-",rotate(arr,d))