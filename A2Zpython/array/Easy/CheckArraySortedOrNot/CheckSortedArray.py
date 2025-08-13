def check(arr):
    result=True
    for i in range(len(arr)-1):
        if(arr[i]>arr[i+1]):
           result=False
           break
    return result





arr=[1,4,5,6,7,1]
print("array is sorted?:",check(arr))