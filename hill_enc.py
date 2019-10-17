import numpy as np
import math

def hillEnc(msg: str, key:list):
    if (int((math.sqrt(len(key)) + .3)) ** 2) != len(key):
        raise Exception("Key Matrix is not square")
    msg = msg.replace(" ", "").upper()
    n = int(math.sqrt(len(key)) + .3)
    mtx = np.array(key).reshape(n, n)

    if (len(msg)%n != 0):
        msg += "X"*(n - len(msg)%n)

    c_arr = []
    for i in range(0, len(msg), n):
        tmpArr = [(ord(c)-65) for c in msg[i:i+n]]
        tmpNp = np.array(tmpArr).reshape(n, 1)
        resArr = np.remainder(mtx.dot(tmpNp), 26)
        for rc in np.nditer(resArr):
            c_arr.append(chr(65 + rc))
    return ''.join(c_arr)
