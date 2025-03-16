def insertionSort(arr):
    n = len(arr)      
    if n <= 1:
        return  
    for i in range(1, n):  
        index = arr[i] 
        j = i-1
        while j >= 0 and index < arr[j]:  
            arr[j+1] = arr[j]  
            j -= 1
        arr[j+1] = index
 

arr = [6,2006, 2,6,102,53,49,43,65,12,202]
insertionSort(arr)
print(arr)
