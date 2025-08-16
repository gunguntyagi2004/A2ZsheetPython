import math;
def buyAndSell(arr):
    maxprofit=0
    bestbuy=arr[0]
    for i in range(1,len(arr)):
        if(arr[i]>bestbuy):
            maxprofit=max(maxprofit,arr[i]-bestbuy)
        else:
            bestbuy=min(bestbuy,arr[i])

    return bestbuy


arr=[7,1,5,3,6,4]
print("buy at:-",buyAndSell(arr))