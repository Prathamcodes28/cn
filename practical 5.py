def binary_search(arr,x):
    LB=0
    UB=len(arr)-1
    MID=0
    while LB<=UB:
        MID=(UB+LB)
        if arr[MID]<x:
            LB=MID+1
        elif arr[MID]>x:
            UB=MID-1
        else:
            return MID
    return-1
arr=[10,20,30,40,50,60,70]
x=int(input("enter number :"))
result=binary_search(arr,x)
if result!=-1:
    print("element is present at index", str(result))
else:
    print("element is not present in arrya")
