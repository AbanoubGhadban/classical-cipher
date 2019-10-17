def vernam_enc(msg:str, key:str):
    msg = msg.replace(" ", "").upper()
    key = key.replace(" ", "").upper()
    if len(key) > len(msg):
        key = key[0:len(msg)]
    assert len(msg) == len(key), "Length of messaga must be the same as length of key"
    
    c_str = []
    for cm, ck in zip(msg, key):
        tmp = (ord(cm) - 65)^(ord(ck) - 65)
        c_str.append(chr(tmp + 65))
    return ''.join(c_str)
