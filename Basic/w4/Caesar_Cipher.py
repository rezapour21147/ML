
Alphabet_list = ['A' , 'B' , 'C' , 'D' , 'E' , 'F' , 'G' , 'H' , 'I' , 'J' , 'K' , 'L' , 'M' , 'N' , 'O' , 'P' , 'Q' , 'R' , 'S' , 'T' , 'U' , 'V' , 'W' , 'X' , 'Y' , 'Z']


def Cryptography(text:str , key:int) -> str:
    list_of_text = list(text)
    for i in range(len(list_of_text)):
        if list_of_text[i] in Alphabet_list:
            list_of_text[i] = Alphabet_list[(Alphabet_list.index(list_of_text[i]) + key) % 26]
    crypted_text = ''.join(list_of_text)
    return crypted_text



def Decryption(text:str , key:int) -> str:
    list_of_text = list(text)
    for i in range(len(list_of_text)):
        if list_of_text[i] in Alphabet_list:
            list_of_text[i] = Alphabet_list[(Alphabet_list.index(list_of_text[i]) - key) % 26]
    uncrypted_text = ''.join(list_of_text)
    return uncrypted_text



