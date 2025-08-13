arr = [64, 25, 12, 22, 11]
print("Original:", arr)


def selection_sort(a):
     for i in range(len(a)):
          
          minindx=i
          for  j in range(i+1,len(a)):
               if(a[j]<a[minindx]):
                    
                    minindx=j
          a[i],a[minindx]=a[minindx],a[i]  

     return a            

sorted_arr = selection_sort(arr)
print("Sorted:", sorted_arr)