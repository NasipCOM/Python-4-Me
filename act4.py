inp=list(map(int, input().split()))

array1=list(map(int, input().split()[:inp[0]]))
array2=list(map(int, input().split()[:inp[0]]))
result = []
for i in range (len(array2) - 1):
    for j in range (len(array1) - 1):
        try:
            if array1[i] == array2[i] and array2.index(j) - inp[2] >= array2[j]  and array2.index(j) + inp[2] >= array2[j]:
                print(array2.index(j))
                result.append(array1[i])
        except:
            pass
print(array1)
print(array2)
print(result)