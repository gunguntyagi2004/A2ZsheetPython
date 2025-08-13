
def find_secondLargest(arr):
   largest=float('-inf')
   secondlargest=-1
   for i in range(len(arr)):
      if(arr[i]>largest):
         largest=arr[i]
      elif(arr[i]<largest and arr[i]>secondlargest):
         secondlargest=arr[i]
   return secondlargest         
      




arr=[8,8,7,6,5]
print("second largest element is:",find_secondLargest(arr))