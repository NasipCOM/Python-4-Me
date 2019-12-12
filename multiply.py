
def multiplies(lenOf, num):
    num.pop(0)
    multiplies = 0
    for i in range(1, lenOf):
        for j in num:
            if j == 0:
                break
            if i % j == 0:
                multiplies += i
                break
    return multiplies

array=list(map(int, input().split()))
lenOf = array[0]
print(multiplies(lenOf, array))