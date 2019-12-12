num = (int(input()))
def collatz_sequence(x):
    num_seq = [x]
    if x < 1:
       return []
    while x > 1:
       if x % 2 == 0:
         x = x / 2
       else:
         x = 3 * x + 1
    
       num_seq.append(x) 
    return len(num_seq) - 1


print(collatz_sequence(num))