# def rotateMatrix(arr):
   
#     m=len(arr)
#     n=len(arr[0])
#     ans = [[0] * m for _ in range(n)]

#     for i in range(m):
#         for j in range(n):
#             ans[j][m-1-i]=arr[i][j]
#     return ans


def rotateMatrix(arr):
    m=len(arr)
    n=len(arr[0])
    for i in range(len(arr)):
        for j in range(i+1,n):
            temp=0
            temp=arr[i][j]
            arr[i][j]=arr[j][i]
            arr[j][i]=temp
   
    for i in range(m):
        for j in range(n//2):
            temp=0
            temp=arr[i][j]
            arr[i][j]=arr[i][n-1-j]
            arr[i][n-1-j]=temp
    return arr        







arr=[[1,2,3],[4,5,6],[7,8,9]]
print("before",arr)
print("after",rotateMatrix(arr))