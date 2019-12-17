

def largest_product(series, size):
	largest = 0
	for i in range(len(series)-size+1):
		temp = 1
		for j in range(size):
			temp *= int(series[i+j]) 
		if temp > largest:
			largest = temp
	return largest
    
number = input().strip()
number, length = number.split(' ')

print(largest_product(number, int(length)))

