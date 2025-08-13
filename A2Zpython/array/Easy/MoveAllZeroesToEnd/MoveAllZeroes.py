
#     Brute Force

# def move(arr):
#     temp=[]
#     for i in range(len(arr)):
#         if(arr[i]!=0):
#             temp.append(arr[i])
    
#     nz=len(temp)
#     for i in range(nz):
#         arr[i]=temp[i]
#     for i in range(nz,len(arr)):
#         arr[i]=0
#     return arr





def move(arr):
    i=0
    for j in range(len(arr)):
        if(arr[j]!=0):
            arr[i]=arr[j]
            i+=1
    
    for k in range(i,len(arr)):
        arr[k]=0

    return arr



arr=[1,0,2,3,0,4,0,1]
print("before:",arr)
print("after:-",move(arr))