def bubble(arr1):
    n=len(arr1)
    for i in range(n):
        swapped=False
        for j in range(0,n-i-1):
            if arr1[j]>arr1[j+1]:
                arr1[j],arr1[j+1]=arr1[j+1],arr1[j]
                swapped=True
        if not swapped:
            break
arr1=[40,60,20,10,83,5]
bubble(arr1)
print("sorted array is:",arr1)
