#--------------------------
# Your Name and ID   <--------------------- Change this -----
# CP460 (Fall 2019)
# Assignment 3
#--------------------------

import math
import string
from utilities_A3 import *

#---------------------------------
#  Q1: Columnar Transposition    #
#---------------------------------
#-----------------------------------------------------------
# Parameters:   key (string)           
# Return:       keyOrder (list)
# Description:  checks if given key is a valid columnar transposition key 
#               Returns key order, e.g. [face] --> [1,2,3,0]
#               Removes repititions and non-alpha characters from key
#               If empty string or not a string -->
#                   print an error msg and return [0] (which is a)
#               Upper 'A' and lower 'a' are the same order
#-----------------------------------------------------------
def get_keyOrder_columnarTrans(key):
    #Check if it is a valid key
    if (not isinstance(key, str)):
        print("Error: Invalid Columnar Transposition Key ", end = '')
        return [0]

    newStr = ""
    for char in key:
        if char.isalpha() and char not in newStr:
            newStr += char.lower()

    if (newStr == ""):
        print("Error: Invalid Columnar Transposition Key ", end = '')
        return [0]

    newStr2 = newStr
    keyOrder = []

    newStr2 = sorted(newStr2)

    for char in newStr2:
        keyOrder.append(newStr.index(char))

    return keyOrder

#-----------------------------------------------------------
# Parameters:   plaintext (str)
#               kye (str)
# Return:       ciphertext (list)
# Description:  Encryption using Columnar Transposition Cipher
#-----------------------------------------------------------
def e_columnarTrans(plaintext,key):
    keyArray = get_keyOrder_columnarTrans(key)    

    size = len(keyArray)

    for i in range(size - (len(plaintext) % len(keyArray))):
        plaintext += 'q'

    plainArray = text_to_blocks(plaintext,size)
    
    ciphertext = ""
    for i in range(size):
        for j in range(len(plainArray)):
            ciphertext += plainArray[j][keyArray[i]]

    return ciphertext

#-----------------------------------------------------------
# Parameters:   ciphertext (str)
#               kye (str)
# Return:       plaintext (list)
# Description:  Decryption using Columnar Transposition Cipher
#-----------------------------------------------------------
def d_columnarTrans(ciphertext,key):
    keyArray = get_keyOrder_columnarTrans(key)    

    size = int(len(ciphertext)/len(keyArray))

    cipherArray = text_to_blocks(ciphertext,size)

    plaintext = ""
    for i in range(size):
        for j in range(len(cipherArray)):
            plaintext += cipherArray[keyArray.index(j)][i]
    
    while plaintext[-1] == 'q':
        plaintext = plaintext[:-1]
        
    return plaintext


#---------------------------------
#   Q2: Permutation Cipher       #
#---------------------------------

#-----------------------------------------------------------
# Parameters:   plaintext (str)
#               key(key,mode)
# Return:       ciphertext (str)
# Description:  Encryption using permutation cipher
#               mode 0: stream cipher --> columnar transposition
#               mode 1: block cipher --> block permutation
#               a padding of 'q' is to be used whenever necessary
#-----------------------------------------------------------
def e_permutation(plaintext,key):
    if not key[0].isdigit():
        print("Error: (e_permutation): Invalid key")
        ciphertext = ''

    elif key[1] == 0:
        keyword = ""
        alpha = get_lower()
        for num in key[0]:
            keyword += alpha[int(num)]
        ciphertext = e_columnarTrans(plaintext,keyword)
    
    elif key[1] == 1:

        keyArray = [-1]*len(key[0])
        for i in range(len(key[0])):
            keyArray[key[0].index( sorted(key[0])[i] )] = i
        
        for i in range(len(keyArray) - (len(plaintext) % len(keyArray))):
            plaintext += 'q'

        size = len(keyArray)
        plainArray = text_to_blocks(plaintext,size)

        ciphertext = ""
        for i in range(len(plainArray)):
            for j in range(size):
                ciphertext += plainArray[i][keyArray[j]]
    
    else:
        print("Error (e_permutation): invalid mode")
        ciphertext = ''
    
    return ciphertext

#-----------------------------------------------------------
# Parameters:   ciphertext (str)
#               key(key,mode)
# Return:       plaintext (str)
# Description:  Decryption using permutation cipher
#               mode 0: stream cipher --> columnar transposition
#               mode 1: block cipher --> block permutation
#               a padding of 'q' is to be removed
#-----------------------------------------------------------
def d_permutation(ciphertext,key):
    if not key[0].isdigit():
        print("Error: (e_permutation): Invalid key")
        plaintext = ''
        
    elif key[1] == 0:
        keyword = ""
        alpha = get_lower()
        for num in key[0]:
            keyword += alpha[int(num)]
        plaintext = d_columnarTrans(ciphertext,keyword)
    
    elif key[1] == 1:

        keyArray = [-1]*len(key[0])
        for i in range(len(key[0])):
            keyArray[key[0].index( sorted(key[0])[i] )] = i    
        
        size = len(keyArray)
        cipherArray = text_to_blocks(ciphertext,size)

        plaintext = ""
        for i in range(len(cipherArray)):
            for j in range(size):
                plaintext += cipherArray[i][keyArray.index(j)]
        
        while plaintext[-1] == 'q':
            plaintext = plaintext[:-1]
    
    else:
        print("Error (e_permutation): invalid mode")
        plaintext = ''

    return plaintext

#---------------------------------
#       Q3: ADFGVX Cipher        #
#---------------------------------
#--------------------------------------------------------------
# Parameters:   plaintext(string)
#               key (string)
# Return:       ciphertext (string)
# Description:  Encryption using ADFGVX cipher
#--------------------------------------------------------------
def e_adfgvx(plaintext, key):
    square = get_adfgvx_square()
    newChars = ['A', 'D', 'F', 'G', 'V', 'X']

    ciphertext = ""
    for char in plaintext:
        if char.isalpha():
            
            foundChar = (-1, -1)
            for i in range(6):
                for j in range(6):
                    if square[i][j] == char.upper():
                        foundChar = (i, j)
                        break
                
                if foundChar != (-1, -1):
                    break
            
            if char.isupper():
                ciphertext += newChars[foundChar[0]]
                ciphertext += newChars[foundChar[1]]
            else:
                ciphertext += newChars[foundChar[0]].lower()
                ciphertext += newChars[foundChar[1]].lower()
        
        elif char.isdigit():
            foundChar = (-1, -1)
            for i in range(6):
                for j in range(6):
                    if square[i][j] == char:
                        foundChar = (i, j)
                        break
                
                if foundChar != (-1, -1):
                    break
            
            ciphertext += newChars[foundChar[0]]
            ciphertext += newChars[foundChar[1]]
        
        else:
            ciphertext += char

    ciphertext = e_columnarTrans(ciphertext, key)

    return ciphertext

#--------------------------------------------------------------
# Parameters:   ciphertext(string)
#               key (string)
# Return:       plaintext (string)
# Description:  Decryption using ADFGVX cipher
#--------------------------------------------------------------
def d_adfgvx(ciphertext, key):

    ciphertext = d_columnarTrans(ciphertext, key)

    square = get_adfgvx_square()
    cipherArray = ['A', 'D', 'F', 'G', 'V', 'X']

    plaintext = ""
    i = 0
    while i < len(ciphertext):
        if (ciphertext[i].isalpha() and ciphertext[i+1].isalpha()):

            indexes = (cipherArray.index(ciphertext[i].upper()), cipherArray.index(ciphertext[i+1].upper()))

            if ciphertext[i].isupper():
                plaintext += square[indexes[0]][indexes[1]]
            else:
                plaintext += square[indexes[0]][indexes[1]].lower()
            
            i += 2
        
        else:
            if not ciphertext[i].isalpha():
                plaintext += ciphertext[i]
            i += 1
    return plaintext

#---------------------------------
#       Q4: One Time Pad         #
#---------------------------------
#--------------------------------------------------------------
# Parameters:   plaintext(string)
#               key (string)
# Return:       ciphertext (string)
# Description:  Encryption using One Time Pad
#               Result is shifted by 32
#--------------------------------------------------------------
def e_otp(plaintext,key):

    if len(plaintext) != len(key):
        print("Error in e_otp: plaintext length does not match key length")
        return ""

    newChar = ""
    ciphertext = ""
    for i in range(len(plaintext)):
        if plaintext[i] != '\n':
            newChar = xor_otp(plaintext[i],key[i])
            newChar = chr(ord(newChar) + 32)
            ciphertext += newChar
                
    return ciphertext

#--------------------------------------------------------------
# Parameters:   ciphertext(string)
#               key (string)
# Return:       plaintext (string)
# Description:  Decryption using One Time Pad
#               Input is shifted by 32
#--------------------------------------------------------------
def d_otp(ciphertext,key):

    if len(ciphertext) != len(key):
        print("Error in e_otp: plaintext length does not match key length")
        return ""

    newChar = ""
    plaintext = ""
    for i in range(len(ciphertext)):
        if ciphertext[i] != '\n':
            newChar = chr(ord(ciphertext[i]) - 32)
            newChar = xor_otp(newChar,key[i])
            plaintext += newChar
    return plaintext
#--------------------------------------------------------------
# Parameters:   char1 (str)
#               char2 (str)
# Return:       result (str)
# Description:  Takes two characters. Convert their corresponding
#               ASCII value into binary (8-bits), then performs xor
#               operation. The result is treated as an ASCII value
#               which is converted to a character
#--------------------------------------------------------------
def xor_otp(char1,char2):
    result = chr(ord(char1) ^ ord(char2))
    return result

#---------------------------------
#    Q5: Myszkowski Cipher      #
#---------------------------------
#-----------------------------------------------------------
# Parameters:   key (string)           
# Return:       keyOrder (list)
# Description:  checks if given key is a valid Myszkowski key 
#               Returns key order, e.g. [meeting] --> [3,0,0,5,2,4,1]
#               The key should have some characters that are repeated
#               and some characters that are non-repeated. 
#               if invalid key --> return [1,1,0]
#               Upper and lower case characters are considered of same order
#               non-alpha characters sould be ignored
#-----------------------------------------------------------
def get_keyOrder_myszkowski(key):

    #Check for invalid var type
    if not isinstance(key, str):
        print("Error: Invalide Myszkowski Key ", end='')
        return [1, 1, 0]

    doubleFlag = False
    singleFlag = False

    newKey = ""
    for char in key:
        if char.isalpha():
            newKey += char.lower()

    #Check for invalid key length
    if len(newKey) <= 1:
        print("Error: Invalide Myszkowski Key ", end='')
        return [1, 1, 0]

    keyOrder = []

    #Check for unique and repeated characters
    for i in range(len(newKey)):

        
        if (newKey.count(newKey[i]) > 1):
            doubleFlag = True
        else:
            singleFlag = True

    if not doubleFlag or not singleFlag:
        print("Error: Invalide Myszkowski Key ", end='')
        return [1, 1, 0]

    #Get key
    for i in range(len(newKey)):

        newVal = 0
        for j in range(len(keyOrder)):

            #Increment old value if new character is less and not already in array
            if newKey[i] < newKey[j] and newKey[i] not in newKey[:i]:
                keyOrder[j] += 1

            #Increment new value if new character is greater and not already in the array
            elif newKey[i] > newKey[j] and newKey[j] not in newKey[:j]:
                newVal += 1

        keyOrder.append(newVal)

    return keyOrder

#--------------------------------------------------------------
# Parameters:   plaintext(string)
#               key (string)
# Return:       ciphertext (string)
# Description:  Encryption using Myszkowsi Transposition
#--------------------------------------------------------------
def e_myszkowski(plaintext,key):
    
    keyArray = get_keyOrder_myszkowski(key)

    size = len(keyArray)

    #Pad text
    for i in range(size - (len(plaintext) % len(keyArray))):
        plaintext += 'q'

    height = int((len(plaintext)/len(keyArray)))

    #Create Array
    tableArray = []*height
    for i in range(height):
        tableArray.append(['']*size)

    #Fill Array
    charCount = 0
    for i in range(height):
        for j in range(size):
            tableArray[i][j] = plaintext[charCount]
            charCount += 1  

    ciphertext = ""
    for i in range(size):
        if (i in keyArray):
            keyi = keyArray.index(i)
            if keyArray.count(i) > 1:

                #Get columns to read together
                indexes = []
                for j in range(size):
                    if (i == keyArray[j]):
                        indexes.append(j)
                

                #Read columns
                for j in range(height):
                    for column in indexes:
                        ciphertext += tableArray[j][column]

            else:
                #columns, rows
                for j in range(height):
                    ciphertext += tableArray[j][keyi]


    return ciphertext

#--------------------------------------------------------------
# Parameters:   ciphertext(string)
#               key (string)
# Return:       plaintext (string)
# Description:  Decryption using Myszkowsi Transposition
#--------------------------------------------------------------
def d_myszkowski(ciphertext,key):
    keyArray = get_keyOrder_myszkowski(key)

    size = len(keyArray)
    height = int((len(ciphertext)/len(keyArray)))

    #Create Array
    tableArray = []*height
    for i in range(height):
        tableArray.append(['']*size)

    #Fill Array
    charCount = 0
    for i in range(size):

        if (i in keyArray):
            keyi = keyArray.index(i)

            if keyArray.count(i) > 1:
                #Get columns to fill together
                indexes = []
                for j in range(size):
                    if (i == keyArray[j]):
                        indexes.append(j)

                #Fill columns
                for j in range(height):
                    for column in indexes:
                        tableArray[j][column] = ciphertext[charCount]
                        charCount += 1

            else:
                for j in range(height):
                    tableArray[j][keyi] = ciphertext[charCount]
                    charCount += 1

    #Get Plaintext
    plaintext=""
    for i in range(height):
        for j in range(size):
            plaintext += tableArray[i][j]

    while plaintext[-1] == 'q':
        plaintext = plaintext[:-1]
    
    return plaintext
