size1 = int(input())
arr1=list(map(int, input().split()[:size1]))
size2 = int(input())
arr2=list(map(int, input().split()[:size2]))


finalArr = []
for i in range (len(arr1)):
    for j in range (len(arr2)):
        if arr1[i] == arr2[j]:
            break
    if (j == len(arr2) - 1): 
            print(arr1[i], end = " ")
            
for i in range (len(arr2)):
    for j in range (len(arr1)):
        if arr2[i] == arr1[j]:
            break
    if (j == len(arr1) - 1): 
            print(arr2[i], end = " ")
  
