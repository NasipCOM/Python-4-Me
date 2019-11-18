def insertionSort(alist):

   for i in range(1,len(alist)):

       current = alist[i]

       while i>0 and alist[i-1]>current:
           alist[i] = alist[i-1]
           i = i-1
           alist[i] = current
          
   return alist

arrLen = int(input())
array=list(map(int, input().split()[:arrLen]))
print(insertionSort(array))
