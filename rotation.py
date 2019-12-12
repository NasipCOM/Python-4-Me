# array=list(map(str, input().split()))
# shift = int(array[0])
# plainText = array[1]
# def caesar(plainText, shift): 
#     for ch in plainText:
#         if ch.isalpha():
#             stayInAlphabet = ord(ch) + shift 
#             if stayInAlphabet > ord('z'):
#                 stayInAlphabet -= 26
#             finalLetter = chr(stayInAlphabet)
#         cipherText = ""
#         cipherText += finalLetter

#     print ("Your ciphertext is: ", cipherText)

#     return cipherText

# caesar(plainText, shift)
#https://gist.github.com/nchitalov/2f2b03e5cf1e19da1525

string = input()
key = 0
for i in string.split(' '):
    if i.isdigit():
        key = int(i)
        string = string.replace(i,'')
plain_text = string.strip()

def caesar_encrypt(step,realText):
	outText = []
	cryptText = []
	
	uppercase = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
	lowercase = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

	for eachLetter in realText:
		if eachLetter in uppercase:
			index = uppercase.index(eachLetter)
			crypting = (index + step) % 26
			cryptText.append(crypting)
			newLetter = uppercase[crypting]
			outText.append(newLetter)
		elif eachLetter in lowercase:
			index = lowercase.index(eachLetter)
			crypting = (index + step) % 26
			cryptText.append(crypting)
			newLetter = lowercase[crypting]
			outText.append(newLetter)
	return ' '.join(outText)

code = caesar_encrypt(key, plain_text)

print()
print(code, end="")
print()

