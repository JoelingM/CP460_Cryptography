from cryptoUtil import get_lower, shift_string

def get_vigenere():
    alphabet = get_lower()
    return [shift_string(alphabet, i, 'l') for i in range(26)]

def e_vigenere(plaintext, key):
    if (key=='' or not key.isalpha()):
        print("Error (e_vigenere): Invalid Key!")
        return ''

    key = key.lower()
    if (len(key) == 1):
        return e_vigenere1(plaintext, key)
    else:
        return e_vigenere2(plaintext, key)

"""
Version 1 (Singel Char)
"""
def e_vigenere1(plaintext, key):
    square = get_vigenereSquare()

    ciphertext = ''
    for char in plaintext:
        #In the alphabet
        if (char.lower in square[0]):
            plainIndx = square[0].index(char.lower())
            keyIndx = square[0].index(key)
            cipherChar = square[keyIndx][plainIndx]
            ciphertext += cipherChar.upper() if char.isupper() else cipherChar
            key = char.lower()
        #Punctuation
        else:
            ciphertext += char
    return ciphertext

def d_vigenere1(ciphertext, key):
    square = get_vigenereSquare()

    plaintext = ''
    for char in ciphertext:
        #In the alphabet
        if (char.lower in square[0]):
            keyIndx = square[0].index(key)
            plainIndx = 0
            for i in range(26):
                if square[i][keyIndx] == char.lower():
                    plainIndx = i
                    break

            plainChar = square[0][plainIndx]
            key = plainChar
            plaintext += plainChar.upper() if char.isupper() else plainChar
        #Punctuation
        else:
            plaintext += char
    return plaintext
