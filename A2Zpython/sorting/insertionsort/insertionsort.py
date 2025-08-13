arr = [64, 25, 12, 22, 11]
print("Original:", arr)


def insertion_sort(a):
     for i in range(1,len(a)):
          
          j=i
          while(j>0 and a[j]<a[j-1]):
               a[j],a[j-1]=a[j-1],a[j]
               j=j-1
     return a           

sorted_arr = insertion_sort(arr)
print("Sorted:", sorted_arr)