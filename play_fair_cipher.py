from string import ascii_uppercase

def _createMatrix(key: str):
    cset = set()
    m = []
    charsMap = {}

    for c in key:
        if (not (c in cset)):
            cset.add(c)
            charsMap[c] = len(m)
            m.append(c)
    
    for c in ascii_uppercase:
        if (c == 'J' or (c == 'I' and 'J' in cset)):
            continue
        if (not (c in cset)):
            cset.add(c)
            charsMap[c] = len(m)
            m.append(c)
    return m, charsMap

def _down(i):
    return (i + 5)%25
def _right(i):
    return (i - 4) if i%5 == 4 else (i + 1)

def _indexOfStr(s: str, sub: str):
    try:
        return s.index(sub)
    except ValueError:
        return -1
    
def _prepareKeyAndText(key: str, text: str):
    key = key.upper().replace(" ", "")
    text = text.upper().replace(" ", "")

    c_arr = [text[0]]
    for i in range(1, len(text)):
        if (text[i] == c_arr[len(c_arr) - 1]):
            c_arr.append("X")
        c_arr.append(text[i])
    if len(c_arr)%2 == 1:
        c_arr.append("X")
    text = ''.join(c_arr)

    ki = _indexOfStr(key, "I")
    kj = _indexOfStr(key, "J")
    if (kj > -1 and (kj < ki or ki == -1)):
        return key.replace("I", "J"), text.replace("I", "J")
    return key.replace("J", "I"), text.replace("J", "I")

def playFairEnc(text: str, key: str):
    key, text = _prepareKeyAndText(key, text)
    print("Prepared Key: {}, Text: {}".format(key, text))
    m, charsMap = _createMatrix(key)

    c_arr = []
    for i in range(0, len(text), 2):
        c1 = charsMap[text[i]]
        c2 = charsMap[text[i+1]]

        rowc1, colc1 = c1//5, c1%5
        rowc2, colc2 = c2//5, c2%5
        if (rowc1 != rowc2 and colc1 != colc2):
            c_arr.append(m[rowc1*5 + colc2])
            c_arr.append(m[rowc2*5 + colc1])
        elif(rowc1 == rowc2):
            c_arr.append(m[_right(c1)])
            c_arr.append(m[_right(c2)])
        else: # The same column
            c_arr.append(m[_down(c1)])
            c_arr.append(m[_down(c2)])
    return ''.join(c_arr)
