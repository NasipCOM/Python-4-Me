
def subCipher():
    key = inputs()
    text_size = int(input())
    plain_text_list = []
    encrypted_text = []
    
    for i in range(text_size):
        text = input()
        plain_text_list.append(text)

    for i in range(len(plain_text_list)):
        simple_string = plain_text_list[i]
        encryption_string = ""
        
        for j in range(len(simple_string)):
            if simple_string[j] in key:
                char_index = key.find(simple_string[j])
                if len(key) - 1 == char_index:
                    char_index = -1

                encryption_string = encryption_string[:j] + key[char_index + 1]
            else:
                encryption_string = encryption_string[:j] + simple_string[j]
        encrypted_text.append(encryption_string)
    return encrypted_text


def inputs():
    key_size = int(input())
    key_input = input()

    return key_input

print(subCipher())
