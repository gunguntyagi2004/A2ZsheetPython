# arr = [10, 45, 2, 99, 67]
# largest = max(arr)
# print("Largest element:", largest)

def largestElement(arr):
    largest=0
    for i in range(len(arr)):
        if(arr[i]>largest):
            largest=arr[i]
    return largest    



arr = [10, 45, 2, 99, 67]
print("Largest element:", largestElement(arr))