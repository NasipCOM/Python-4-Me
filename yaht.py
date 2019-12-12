def inputs():
    inp = input()
    score = [i for i in inp.strip().split(' ')]
    category = score[-1]
    score.pop(-1)
    score = [int(i) for i in score]
    
    return score, category


def remove_duplicates(array):
    return list(dict.fromkeys(array))


def yacht(score, category):
    if category == "YACHT":
        temp = score[0]
        for i in range(len(score)):
            if score[i] == temp:
                pass
            else:
                return 0
        return 50

    if category == "ONES":
        result = 0
        for i in score:
            if i == 1:
                result += i
        return result

    if category == "TWOS":
        result = 0
        for i in score:
            if i == 2:
                result += i
        return result

    if category == "THREES":
        result = 0
        for i in score:
            if i == 3:
                result += i
        return result

    if category == "FOURS":
        result = 0
        for i in score:
            if i == 4:
                result += i
        return result

    if category == "FIVES":
        result = 0
        for i in score:
            if i == 5:
                result += i
        return result
        
    if category == "SIXES":
        result = 0
        for i in score:
            if i == 6:
                result += i
        return result

    if category == "FULL_HOUSE":
        num_array = remove_duplicates(score)
        
        if len(num_array) != 2:
            return 0

        array1 = [score[0]]
        array2 = []
        for i in range(1, len(score)):
            
            if score[i] == array1[0]:
                array1.append(score[i])
            if score[i] != array1[0]:
                array2.append(score[i])
        
        if (len(array1) == 3 and len(array2) == 2) or (len(array2) == 3 and len(array1) == 2):
            return sum(array1) + sum(array2)
        else:
            return 0

    if category == "FOUR_OF_A_KIND":
        num_array = remove_duplicates(score)
        
        if len(num_array) != 2:
            return 0

        array1 = [score[0]]
        array2 = []
        for i in range(1, len(score)):
            
            if score[i] == array1[0]:
                array1.append(score[i])
            if score[i] != array1[0]:
                array2.append(score[i])
        
        if (len(array1) == 4 and len(array2) == 1) or (len(array2) == 4 and len(array1) == 1):
            return sum(array1) + sum(array2)
        else:
            return 0
    
    if category == "LITTLE_STRAIGHT":
        if score[0] == 1:
            for i in range(len(score) - 1):
                if score[i + 1] - score[i] == 1:
                    pass
                else:
                    return 0
            return 30
        else:
            return 0

    if category == "BIG_STRAIGHT":
        if score[0] == 2:
            for i in range(len(score) - 1):
                if score[i + 1] - score[i] == 1:
                    pass
                else:
                    return 0
            return 30
        else:
            return 0

    if category == "CHOICE":
        return sum(score)

score, category = inputs()
print(yacht(score, category))