#Brute Force

# def setMatrix(arr):
#     m = len(arr)
#     n = len(arr[0])

    
#     temp = [row[:] for row in arr]

#     for i  in range(m):
#         for j in range(n):
#             if arr[i][j]==0:
#                 for c in range(n):
#                     temp[i][c]=0
#                 for r in range(m):
#                     temp[r][j]=0


#     for i in range(m):
#         arr[i] = temp[i][:]  # clone

#     return arr


#Better Approach

# def setMatrix(arr):
#     m=len(arr)
#     n=len(arr[0])

#     row=[False]*m
#     col=[False]*n

#     for i in range(m):
#         for j in range(n):
#             if arr[i][j]==0:
#                 row[i]= True
#                 col[j]=True

#     for i in range(m):
#         for j in range(n):
#             if(col[j] or row[i]):
#                 arr[i][j]=0

#     return arr





def setMatrix(arr):
    col0=1
    m=len(arr)
    n=len(arr[0])

    for i in range(m):
        for j in range(n):
            if arr[i][j]==0:
                arr[i][0]=0
                if(j!=0):
                    arr[0][j]=0
                else:
                    col0=0   
   

    for i in range(1,m):
        for j in range(1,n):
            if arr[i][j]!=0:
                if(arr[i][0]==0 or arr[0][j]==0):
                    arr[i][j]=0

    if(arr[0][0]==0):
        for j in range(n):
            arr[0][j]=0

    if(col0==0):
        for i in range(m):
            arr[i][0]=0



  












arr=[[1,1,1,1],[1,0,1,1],[1,1,0,1],[0,1,1,1]]
print("Before:")
for row in arr:
    print(row)

setMatrix(arr)

print("\nAfter:")
for row in arr:
    print(row)