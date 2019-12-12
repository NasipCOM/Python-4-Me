def phone_number(arr):
   
    letters = "qwertyuioppasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM"
    puncutation = "[]{}\|/?>,<=_*&^%$#@!~"
    if len(arr) > 11:
        return "more than 11 digits"

    elif len(arr) == 11 and arr[0] != 1:
        return "11 digits must start with 1"

    elif len(arr) < 10:
        return "incorrect number of digits"

    elif len(arr) == 11:
        arr.pop(0)    

    elif  arr[0] == 0:
        return "area code cannot start with zero"

    elif arr[0] == 1:
        return "area code cannot start with one"

    elif arr[3] == 0:
        return "exchange code cannot start with zero"

    elif arr[3] == 1:
        return "exchange code cannot start with one"

    for i in arr:
        print(i, end='')



def my_input():
    num = input()

    letters = "qwertyuioppasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM"
    puncutation = "[]{}\|/?>,<=_*&^%$#@!~"

    for i in letters:
        if i in num:
            return "letters not permitted"

    for i in puncutation:
        if i in num:
            return "punctuations not permitted"

    numlist = [int(i) for i in num if i.isdigit()]
    return numlist


print(phone_number(my_input()))
