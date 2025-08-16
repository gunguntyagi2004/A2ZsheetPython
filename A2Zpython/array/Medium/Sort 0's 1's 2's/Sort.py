
#   Brute Force
# def sort(arr):
#    return  sorted(arr)


# Better Approach

# def sort(arr):
#     count0=0
#     count1=0
#     count2=0
#     for i in range(len(arr)):
#       if arr[i]==0:
#          count0+=1
#       elif arr[i]==1:
#          count1+=1
#       else:
#          count2+=1    
#     indx=0       
#     for i in range(count0):
#        arr[indx]=0
#        indx+=1
#     for i in range(count1):
#        arr[indx]=1
#        indx+=1
#     for i in range(count2):
#        arr[indx]=2
#        indx+=1   
#     return arr

def swap(arr,i,j):
    arr[i],arr[j]=arr[j],arr[i]
    

def sort(arr):
    mid=0
    low=0
    high=len(arr)-1

    while(mid<=high):
        if(arr[mid]==0):
            swap(arr,mid,low)
            mid+=1
            low+=1
        elif (arr[mid]==1):
            mid+=1
        else:
            swap(arr,mid,high)
            high-=1        
    return arr

 


arr=[1,0,1,2,0,1]
print("sorted array is :",sort(arr))
