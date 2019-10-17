import os
from caeser_enc import caesarEnc
from play_fair_cipher import playFairEnc
from hill_enc import hillEnc
from vigenere_enc import vigenere_enc
from vernam_enc import vernam_enc

def performCaesarCipher():
    if (not os.path.exists("output/Caesar")):
        os.makedirs("output/Caesar")

    for key in (3, 6, 12):
        f = open("input/Caesar/caesar_plain.txt", "r")
        fo = open("output/Caesar/cipher_" + str(key) + ".txt", "w+")
        conents = f.read()
        for line in conents.split("\n"):
            if str.strip(line) == "":
                continue
            fo.write(caesarEnc(line, key))
            fo.write("\n")
        f.close()
        fo.close()

def performPlayFairCipher():
    if (not os.path.exists("output/PlayFair")):
        os.makedirs("output/PlayFair")
    for key in ("rats", "archangel"):
        f = open("input/PlayFair/playfair_plain.txt", "r")
        fo = open("output/PlayFair/playfair_" + key + ".txt", "w+")
        contents = f.read()
        for line in contents.split("\n"):
            if str.strip(line) == "":
                continue
            fo.write(playFairEnc(line, key))
            fo.write("\n")
        f.close()
        fo.close()

def performHillCipher():
    if (not os.path.exists("output/Hill")):
        os.makedirs("output/Hill")
    for dim, key in zip([2, 3], [[5, 17, 8, 3], [2, 4, 12, 9, 1, 6, 7, 5, 3]]):
        dimStr = str(dim) + "x" + str(dim)
        f = open("input/Hill/hill_plain_" + dimStr + ".txt", "r")
        fo = open("output/Hill/hill_" + dimStr + ".txt", "w+")
        contents = f.read()
        for line in contents.split("\n"):
            if str.strip(line) == "":
                continue
            fo.write(hillEnc(line, key))
            fo.write("\n")
        f.close()
        fo.close()

def performVigenereCipher():
    if (not os.path.exists("output/Vigenere")):
        os.makedirs("output/Vigenere")
    for repeating, key in zip([True, False], ["pie", "aether"]):
        f = open("input/Vigenere/vigenere_plain.txt", "r")
        fo = open("output/Vigenere/vigenere_" + key + ".txt", "w+")
        contents = f.read()
        for line in contents.split("\n"):
            if str.strip(line) == "":
                continue
            fo.write(vigenere_enc(line, key, repeating))
            fo.write("\n")
        f.close()
        fo.close()

def performVernamCipher():
    if (not os.path.exists("output/Vernam")):
        os.makedirs("output/Vernam")
    for key in ["SPARTANS"]:
        f = open("input/Vernam/vernam_plain.txt", "r")
        fo = open("output/Vernam/vernam_" + key + ".txt", "w+")
        contents = f.read()
        for line in contents.split("\n"):
            if str.strip(line) == "":
                continue
            fo.write(vernam_enc(line, key))
            fo.write("\n")
        f.close()
        fo.close()

def main():
    performCaesarCipher()
    performPlayFairCipher()
    performHillCipher()
    performVigenereCipher()
    performVernamCipher()
    
if __name__ == "__main__":
    main()
