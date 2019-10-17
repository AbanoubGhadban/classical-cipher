def encrypt_vigenere_word(word:str, key:str):
    c_arr = ['A']*len(word)
    for i in range(len(word)):
        c_arr[i] = chr(65 + ((ord(word[i]) + ord(key[i]))%65)%26)
    return c_arr

def vigenere_enc(msg: str, key: str, repeating: bool):
    msg = msg.replace(" ", "").upper()
    key = key.replace(" ", "").upper()
    n = len(key)

    c_arr = []
    for i in range(0, len(msg), n):
        nextKey = key if (i == 0 or repeating) else ''.join(msg[i - n:i])
        c_arr.extend(encrypt_vigenere_word(msg[i:i+n], nextKey))
    return ''.join(c_arr)
