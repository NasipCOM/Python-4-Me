# x = int(input())
# arrInp = []

# for i in range (x):
#     nums = int(input())
#     arrInp.append(nums)

# def main(arr):
#     for i in range (len(arr)):
#         print(arr[i],(arr[i] * "0"))

# main(arrInp)
def bonus():
    test_cases = int(input())
    num_list = []
    for i in range(test_cases):
        x = int(input())
        num_list.append(x)
    for i in num_list:
        print(i * pow(10, i))

bonus()