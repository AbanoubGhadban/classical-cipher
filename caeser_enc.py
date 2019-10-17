def caesarEnc(text, key):
    key = int(key)
    cipher = []
    for c in text:
        tmpC = ord(c.upper()) + key - ord('A')
        cipher.append(chr(tmpC%26 + ord('A')))
    return ''.join(cipher)
