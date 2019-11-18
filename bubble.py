def bubbleSort(alist): 
    n = len(alist)
    
    for i in range(n): 
        for j in range(0, n-i-1): 

            if alist[j] > alist[j+1] : 
                alist[j], alist[j+1] = alist[j+1], alist[j]
    return alist

arrLen = int(input())
array=list(map(int, input().split()[:arrLen]))
print(bubbleSort(array))
