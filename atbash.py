import string
import re

ENCODE_TABLE = str.maketrans(
    string.ascii_letters,
    ''.join(reversed(string.ascii_lowercase + string.ascii_lowercase)),
    string.punctuation + string.whitespace)

DECODE_TABLE = str.maketrans(
    string.ascii_lowercase,
    ''.join(reversed(string.ascii_lowercase)),
    string.whitespace)

def encoding(text):
    newstr = text.translate(ENCODE_TABLE)
    result = re.findall(r'.{1,5}', newstr)
    return ' '.join(result)

def decoding(encryptedstring):
    return encryptedstring.translate(DECODE_TABLE)    

def main(arr):
    if arr[0] == "Encoding":
        arr.remove(arr[0])
        for i in range (len(arr)):
            print(encoding(arr[i]), end= " ")
    elif arr[0] == "Decoding": 
        arr.remove(arr[0])
        for i in range (len(arr)):
            print(decoding(arr[i]), end="")

array=list(map(str, input().split()))

main(array)

