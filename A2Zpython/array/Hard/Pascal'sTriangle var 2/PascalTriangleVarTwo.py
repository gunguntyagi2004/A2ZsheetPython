def binomialCoeff(n,r):
    res=1
    for i in range(r):
       res=res*(n-i)
       res=res//(i+1)
    return res   








def pascalTriangle(n):
     
     ans=1
     for i in range(n+1):
        if(n==0):
         print(1)
         break
     
        ans=  binomialCoeff(n,i)
        print(ans)










n=int(input("enter the row number"))
print("all elements are:-")
pascalTriangle(n)