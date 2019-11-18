def sum_of(str1):
    sum_digit = 0
    for x in str1:
        if x.isdigit() == True:
            z = int(x)
            sum_digit = sum_digit + z    

    return sum_digit

print(sum_of("12243660"))
print(sum_of("1111112223"))
