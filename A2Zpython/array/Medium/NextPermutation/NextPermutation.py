def reverse(arr,i,j):
    while(i<j):
        arr[i],arr[j]=arr[j],arr[i]
        i+=1
        j-=1

def nextPermutation(arr):
    pivot=-1
    n=len(arr)
    for i in range(n-2,-1,-1):
        if(arr[i]<arr[i+1]):
            pivot=i
            print(pivot)
            break

    if pivot==-1:
        arr.reverse()
        return arr
    
    for i in range(n-1,pivot,-1):
        if(arr[i]>arr[pivot]):
            arr[i],arr[pivot]=arr[pivot],arr[i]
            break

    
    reverse(arr,pivot+1,n-1)
        
    return arr








arr=[1,2,3,6,5,4]
print("next permutation is :-",nextPermutation(arr))