def isbn(list):
    listLen = len(list)

    if len(list) == 10:
        pass
    else:
        return False
        
    result = 0
    
    for i in list:
        result = result + i * listLen
        listLen -= 1

    if result % 11 == 0:
        return True
    else:
        return False


myNum = input()
myList = []
    for i in myNum:
        if i.isdigit():
            number_list.append(int(i))
        if i == 'X':
            number_list.append(10)

print(isbn(myList))
