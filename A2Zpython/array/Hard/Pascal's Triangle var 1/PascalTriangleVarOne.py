# def fact(n):
#     if n==0 or n==1:
#         return 1
#     else:
#         return n*fact(n-1)



# def pascalVarOne(n,r):
#    factn=fact(n)
#    factr=fact(r)
#    factnr=fact(n-r)
#    return factn//(factr*factnr)
        







def pascalVarOne(n,r):
    res=1
    for i in range(r):
        res=res*(n-i)
        res=res//(i+1)
    return res    




n=7
r=4
print("element at nth row and rth column:-",pascalVarOne(n,r))