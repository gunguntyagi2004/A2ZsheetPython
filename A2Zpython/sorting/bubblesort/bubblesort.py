arr = [64, 25, 12, 22, 11]
print("Original:", arr)


def bubble_sort(a):
     for i in range(len(a)):
          for j in range(len(a)-1):
               if(a[j]>a[j+1]):
                    a[j],a[j+1]=a[j+1],a[j]
         
     return a            

sorted_arr = bubble_sort(arr)
print("Sorted:", sorted_arr)