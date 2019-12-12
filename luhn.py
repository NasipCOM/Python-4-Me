def luhnAlg(arr):
    for i in range(0, len(arr), 2):
        temp = arr[i] * 2
        if temp > 9:
            temp -= 9
        arr[i] = temp
    if sum(arr) % 10 == 0:
        return "True"
    else:
        return "False"

num = input()
nums= [int(i) for i in num if i.isdigit()]

print(luhnAlg(nums))