def fun4(number_list1, number_list2, x_list):
    x = x_list[1]
    y = []
    for i in range((x * 2) + 1):
        y.append(x * -1 + i)
    number_list3 = []
    for i in range(len(number_list1)):
        for j in range(len(y)):
            try:
                if number_list1[i] == number_list2[i + y[j]] and i + y[j] >= 0:
                    number_list3.append(i + 1)
            except:
                pass
    return number_list3

def inputs():
    arrLen = input()
    x_list = [int(i) for i in arrLen.strip().split(' ')]
    
    arr1 = input()
    number_list1 = [int(i) for i in arr1.split(' ')]
    
    arr2 = input()
    number_list2 = [int(i) for i in arr2.split(' ')]
    
    return number_list1, number_list2, x_list

def major():
    list1, list2, x_y = inputs()
    restult_list = fun4(list1, list2, x_y)
    for i in restult_list:
        print(i, end=' ')

major()
