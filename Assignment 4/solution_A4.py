#--------------------------
# CP460 (Fall 2019)
# Assignment 4
# Joseph Myc | 160 740 900
#--------------------------

import math
import string
import mod
import matrix
import utilities_A4

#---------------------------------
# Q1: Modular Arithmetic Library #
#---------------------------------

# solution is available in mod.py

#---------------------------------
#     Q2: Decimation Cipher      #
#---------------------------------
#-----------------------------------------------------------
# Parameters:   plaintext (str)
#               key (str,int)
# Return:       ciphertext (str)
# Description:  Encryption using Decimation Cipher
#               key is tuple (baseString,k)
#               Does not encrypt characters not in baseString
#               Case of letters should be preserved
# Errors:       if key has no multiplicative inverse -->
#                   print error msg and return empty string
#-----------------------------------------------------------
def e_decimation(plaintext,key):
    if not mod.has_mul_inv(key[1], len(key[0])):
        print("Error (e_decimation): Invalid key")
        return ""

    ciphertext = ""
    for char in plaintext:
        tempChar = char
        charNum = 0

        if char.isalpha() and char.lower() in key[0]:
            tempChar = tempChar.lower()

            #Get new char index
            charNum = key[0].index(tempChar)
            charNum = (charNum * key[1]) % len(key[0])

            tempChar = key[0][charNum]

            if char.isalpha() and char.isupper():
                tempChar = tempChar.upper()

        elif char in key[0]:

            #Get new char index
            charNum = key[0].index(tempChar)
            charNum = (charNum * key[1]) % len(key[0])

            tempChar = key[0][charNum]

        ciphertext += tempChar

    return ciphertext

#-----------------------------------------------------------
# Parameters:   ciphertext (str)
#               key (str,int)
# Return:       plaintext (str)
# Description:  Decryption using Decimation Cipher
#               key is tuple (baseString,k)
#               Does not decrypt characters not in baseString
#               Case of letters should be preserved
# Errors:       if key has no multiplicative inverse -->
#                   print error msg and return empty string
#-----------------------------------------------------------
def d_decimation(ciphertext,key):
    if not mod.has_mul_inv(key[1], len(key[0])):
        print("Error (d_decimation): Invalid key")
        return ""

    keyin = mod.mul_inv(key[1], len(key[0]))

    plaintext = ""
    for char in ciphertext:
        tempChar = char
        charNum = 0

        if char.isalpha() and char.lower() in key[0]:
            tempChar = tempChar.lower()

            #Get new char index
            charNum = key[0].index(tempChar)
            charNum = (charNum * keyin) % len(key[0])

            tempChar = key[0][charNum]

            if char.isalpha() and char.isupper():
                tempChar = tempChar.upper()

        elif char in key[0]:

            #Get new char index
            charNum = key[0].index(tempChar)
            charNum = (charNum * keyin) % len(key[0])

            tempChar = key[0][charNum]

        plaintext += tempChar

    return plaintext

#-----------------------------------------------------------
# Parameters:   ciphertext (str)
# Return:       plaintext,key
# Description:  Cryptanalysis of Decimation Cipher
#-----------------------------------------------------------
def cryptanalysis_decimation(ciphertext):
    dictList = utilities_A4.load_dictionary("engmix.txt")
    attemptCount = 1

    baseString = utilities_A4.get_baseString()
    for i in range(26, len(baseString), 1):
        tempBaseStr = baseString[:i]

        #Get inverse table
        inv_table = mod.mul_inv_table(i)
        inv_table[1] = filter(lambda x: x != "NA", inv_table[1])
        inv_table[1] = sorted(inv_table[1])

        for j in range(len(inv_table[1])):
            plaintext = d_decimation(ciphertext, (tempBaseStr, inv_table[1][j]))
            if utilities_A4.is_plaintext(plaintext, dictList, 0.9):
                print("key found after", attemptCount, "attempts")
                return plaintext, (tempBaseStr, inv_table[1][j])
            else:
                attemptCount += 1
    return '',''

#---------------------------------
#      Q3: Affine Cipher         #
#---------------------------------
#-----------------------------------------------------------
# Parameters:   plaintext (str)
#               key (str,[int,int])
# Return:       ciphertext (str)
# Description:  Encryption using Affine Cipher
#               key is tuple (baseString,[alpha,beta])
#               Does not encrypt characters not in baseString
#               Case of letters should be preserved
# Errors:       if key can not be used for decryption
#                   print error msg and return empty string
#-----------------------------------------------------------
def e_affine(plaintext,key):
    if not mod.has_mul_inv(key[1][0], len(key[0])):
        print("Error (e_affine): Invalid key")
        return ""

    ciphertext = ""
    for char in plaintext:
        tempChar = char
        charNum = 0

        if char.isalpha() and char.lower() in key[0]:
            tempChar = tempChar.lower()

            #Get new char index
            charNum = key[0].index(tempChar)
            charNum = ((charNum * key[1][0]) + key[1][1]) % len(key[0])

            tempChar = key[0][charNum]

            if char.isalpha() and char.isupper():
                tempChar = tempChar.upper()

        elif char in key[0]:

            #Get new char index
            charNum = key[0].index(tempChar)
            charNum = ((charNum * key[1][0]) + key[1][1]) % len(key[0])

            tempChar = key[0][charNum]

        ciphertext += tempChar

    
    return ciphertext

#-----------------------------------------------------------
# Parameters:   ciphertext (str)
#               key (str,[int,int])
# Return:       plaintext (str)
# Description:  Decryption using Affine Cipher
#               key is tuple (baseString,[alpha,beta])
#               Does not decrypt characters not in baseString
#               Case of letters should be preserved
# Errors:       if key can not be used for decryption
#                   print error msg and return empty string
#-----------------------------------------------------------
def d_affine(ciphertext,key):
    if not mod.has_mul_inv(key[1][0], len(key[0])):
        print("Error (d_affine): Invalid key")
        return ""

    keyin = mod.mul_inv(key[1][0], len(key[0]))

    plaintext = ""
    for char in ciphertext:
        tempChar = char
        charNum = 0

        if char.isalpha() and char.lower() in key[0]:
            tempChar = tempChar.lower()

            #Get new char index
            charNum = key[0].index(tempChar)
            charNum = (keyin * (charNum - key[1][1])) % len(key[0])

            tempChar = key[0][charNum]

            if char.isalpha() and char.isupper():
                tempChar = tempChar.upper()

        elif char in key[0]:

            #Get new char index
            charNum = key[0].index(tempChar)
            charNum = (keyin * (charNum - key[1][1])) % len(key[0])

            tempChar = key[0][charNum]

        plaintext += tempChar

    return plaintext

#-----------------------------------------------------------
# Parameters:   ciphertext (str)
# Return:       plaintext,key
# Description:  Cryptanalysis of Affine Cipher
#-----------------------------------------------------------
def cryptanalysis_affine(ciphertext):
    dictList = utilities_A4.load_dictionary("engmix.txt")
    attemptCount = 1

    baseString = utilities_A4.get_baseString()
    for i in range(26, len(baseString), 1):
        tempBaseStr = baseString[:i]

        #Get inverse table
        inv_table = mod.mul_inv_table(i)
        inv_table[1] = filter(lambda x: x != "NA", inv_table[1])
        inv_table[1] = sorted(inv_table[1])

        for j in range(len(inv_table[1])):
            for k in range(i):
                plaintext = d_affine(ciphertext, (tempBaseStr, [inv_table[1][j], k]))
                if utilities_A4.is_plaintext(plaintext, dictList, 0.9):
                    print("key found after", attemptCount, "attempts")
                    return plaintext, (tempBaseStr, [inv_table[1][j], k])
                else:
                    attemptCount += 1
    return '',''

#---------------------------------
#      Q4: Matrix Library        #
#---------------------------------

# solution is available in matrix.py

#---------------------------------
#       Q5: Hill Cipher          #
#---------------------------------

#-----------------------------------------------------------
# Parameters:   plaintext (str)
#               key (str)
# Return:       ciphertext (str)
# Description:  Encryption using Hill Cipher, 2x2 (mod 26)
#               key is a string consisting of 4 characters
#                   if key is too short, make it a running key
#                   if key is too long, use first 4 characters
#               Encrypts only alphabet
#               Case of characters can be ignored --> cipher is upper case
#               If necessary pad with 'Q'
# Errors:       if key is not inveritble or if plaintext is empty
#                   print error msg and return empty string
#-----------------------------------------------------------
def e_hill(plaintext,key):
    if len(key) > 4:
        key = key[:4]
    elif len(key) < 4 and len(key) > 0:
        i = 0
        while len(key) < 4:
            key = key + key[i]
            i += 1

    elif len(key) < 0:
        print("Error(e_hill): key is not invertible")
        return ""

    if len(plaintext) == 0:
        print("Error(e_hill): invalid plaintext")
        return ""

    alphaString = utilities_A4.get_lower()
    key = key.lower()
    keyArray = matrix.new_matrix(2, 2, 0)
    keyArray[0][0] = alphaString.index(key[0])
    keyArray[0][1] = alphaString.index(key[1])
    keyArray[1][0] = alphaString.index(key[2])
    keyArray[1][1] = alphaString.index(key[3])

    det = keyArray[0][0]*keyArray[1][1] - keyArray[0][1]*keyArray[1][0]
    if mod.mul_inv(det, 26) == "NA":
        print('Error(e_hill): key is not invertible') 
        return ""

    #Format plaintext for encryption
    plaintext = plaintext.lower()
    nonAlpha = utilities_A4.get_nonalpha(plaintext)
    plaintext = utilities_A4.remove_nonalpha(plaintext)
    if len(plaintext) % 2 == 1:
        plaintext += 'q'

    ciphertext = ""
    tempArray = matrix.new_matrix(2, 1, 0)
    for i in range(0, len(plaintext), 2):
        tempArray[0][0] = alphaString.index(plaintext[i])
        tempArray[1][0] = alphaString.index(plaintext[i+1])
    
        newArray = matrix.mul(keyArray, tempArray)

        ciphertext += alphaString[newArray[0][0] % 26]
        ciphertext += alphaString[newArray[1][0] % 26]

    ciphertext = utilities_A4.insert_nonalpha(ciphertext, nonAlpha)

    return ciphertext.upper()

#-----------------------------------------------------------
# Parameters:   ciphertext (str)
#               key (str)
# Return:       plaintext (str)
# Description:  Decryption using Hill Cipher, 2x2 (mod 26)
#               key is a string consisting of 4 characters
#                   if key is too short, make it a running key
#                   if key is too long, use first 4 characters
#               Decrypts only alphabet
#               Case of characters can be ignored --> plain is lower case
#               Remove padding of q's
# Errors:       if key is not inveritble or if ciphertext is empty
#                   print error msg and return empty string
#-----------------------------------------------------------
def d_hill(ciphertext,key):
    if len(key) > 4:
        key = key[:4]
    elif len(key) < 4 and len(key) > 0:
        i = 0
        while len(key) < 4:
            key = key + key[i]
            i += 1

    elif len(key) < 0:
        print("Error(d_hill): key is not invertible")
        return ""

    if len(ciphertext) == 0:
        print("Error(d_hill): invalid ciphertext")
        return ""

    alphaString = utilities_A4.get_lower()
    key = key.lower()
    keyArray = matrix.new_matrix(2, 2, 0)
    keyArray[0][0] = alphaString.index(key[0])
    keyArray[0][1] = alphaString.index(key[1])
    keyArray[1][0] = alphaString.index(key[2])
    keyArray[1][1] = alphaString.index(key[3])

    det = keyArray[0][0]*keyArray[1][1] - keyArray[0][1]*keyArray[1][0]
    if mod.mul_inv(det, 26) == "NA":
        print('Error(d_hill): key is not invertible') 
        return ""
    
    keyArray = matrix.inverse(keyArray, 26)

    #Format plaintext for encryption
    ciphertext = ciphertext.lower()
    nonAlpha = utilities_A4.get_nonalpha(ciphertext)
    ciphertext = utilities_A4.remove_nonalpha(ciphertext)

    plaintext = ""
    tempArray = matrix.new_matrix(2, 1, 0)
    for i in range(0, len(ciphertext), 2):
        tempArray[0][0] = alphaString.index(ciphertext[i])
        tempArray[1][0] = alphaString.index(ciphertext[i+1])
    
        newArray = matrix.mul(keyArray, tempArray)

        plaintext += alphaString[newArray[0][0] % 26]
        plaintext += alphaString[newArray[1][0] % 26]

    plaintext = utilities_A4.insert_nonalpha(plaintext, nonAlpha)
    
    if plaintext[-1] == 'q':
        plaintext = plaintext[:-1]

    return plaintext

