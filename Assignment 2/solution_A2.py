#--------------------------
# Joseph Myc | 160 740 900
# CP460 (Fall 2019)
# Assignment 2
#--------------------------

import math
import string
import utilities_A2

#---------------------------------
#Q1: Vigenere Cipher (Version 2) #
#---------------------------------
#-------------------------------------------------------------------------------------
# Parameters:   plaintext(string)
#               key (str): string of any length
# Return:       ciphertext (string)
# Description:  Genereic Encryption scheme using Vigenere Cipher
#               calls proper function depending on key length
#               if len(key) == 1 --> call e_vigenere1
#               else --> call e_vigenere2
#               If invalid key (not string or empty string or non-alpha string) -->
#                   print error and return '',''
#---------------------------------------------------------------------------------------
def e_vigenere(plaintext, key):
    if not isinstance(key,str) or key == '' or not key.isalpha():
        print('Error (e_vigenere): invalid key!')
        return ''
    key = key.lower()
    if len(key) == 1:
        return e_vigenere1(plaintext,key)
    else:
        return e_vigenere2(plaintext,key)

#-------------------------------------------------------------------------------------
# Parameters:   ciphertext(string)
#               key (str): string of anylength
# Return:       ciphertext (string)
# Description:  Genereic Encryption scheme using Vigenere Cipher
#               calls proper function depending on key length
#               if len(key) == 1 --> call d_vigenere1
#               else --> call d_vigenere2
#               If invalid key (not string or empty string or contains no alpha char) -->
#                   print error and return '',''
#---------------------------------------------------------------------------------------
def d_vigenere(ciphertext,key):
    if not isinstance(key,str) or key == '' or not key.isalpha():
        print('Error (d_vigenere): invalid key!')
        return ''
    key = key.lower()
    if len(key) == 1:
        return d_vigenere1(ciphertext,key)
    else:
        return d_vigenere2(ciphertext,key)

#-------------------------------------------------------------------------------------
# Parameters:   plaintext(string)
#               key (str): single character
# Return:       ciphertext (string)
# Description:  Encryption using Vigenere Cipher (Polyalphabetic Substitituion)
#               Non alpha characters --> no substitution
#               Algorithm preserves case of the characters
#---------------------------------------------------------------------------------------
def e_vigenere1(plaintext, key):
    square = utilities_A2.get_vigenereSquare()

    ciphertext = ''
    for char in plaintext:
        #In the alphabet
        if (char.lower() in square[0]):
            plainIndx = square[0].index(char.lower())
            keyIndx = square[0].index(key)
            cipherChar = square[keyIndx][plainIndx]
            ciphertext += cipherChar.upper() if char.isupper() else cipherChar
            key = char.lower()
        #Punctuation
        else:
            ciphertext += char
            
    return ciphertext

#-------------------------------------------------------------------------------------
# Parameters:   plaintext(string)
#               key (str): a phrase
# Return:       ciphertext (string)
# Description:  Encryption using Vigenere Cipher (Polyalphabetic Substitituion)
#               Non alpha characters --> no substitution
#               Algorithm preserves case of the characters
#---------------------------------------------------------------------------------------
def e_vigenere2(plaintext, key):
    # your code here
    square = utilities_A2.get_vigenereSquare()

    ciphertext = ''
    i = 0
    for char in plaintext:
        #In the alphabet
        if (char.lower() in square[0]):
            #Get the next key character
            keyChar = key[i%len(key)]
            i += 1

            #Use key to encrypt
            plainIndx = square[0].index(char.lower())
            keyIndx = square[0].index(keyChar)
            cipherChar = square[keyIndx][plainIndx]
            ciphertext += cipherChar.upper() if char.isupper() else cipherChar
            #key = char.lower()
        #Punctuation
        else:
            ciphertext += char

    return ciphertext
    
#-------------------------------------------------------------------------------------
# Parameters:   ciphertext(string)
#               key (str): single character
# Return:       ciphertext (string)
# Description:  Decryption using Vigenere Cipher (Polyalphabetic Substitituion)
#               Non alpha characters --> no substitution
#               Algorithm preserves case of the characters
#---------------------------------------------------------------------------------------
def d_vigenere1(ciphertext, key):
    # your code here
    square = utilities_A2.get_vigenereSquare()

    plaintext = ''
    for char in ciphertext:
        #In the alphabet
        if (char.lower() in square[0]):
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

#-------------------------------------------------------------------------------------
# Parameters:   ciphertext(string)
#               key (str): a phrase
# Return:       ciphertext (string)
# Description:  Decryption using Vigenere Cipher (Polyalphabetic Substitituion)
#               Non alpha characters --> no substitution
#               Algorithm preserves case of the characters
#---------------------------------------------------------------------------------------
def d_vigenere2(ciphertext, key):
    # your code here
    square = utilities_A2.get_vigenereSquare()

    plaintext = ''
    j = 0
    for char in ciphertext:
        
        #In the alphabet
        if (char.lower() in square[0]):
            keyChar = key[j%len(key)]
            j += 1
            keyIndx = square[0].index(keyChar)
            plainIndx = 0
            for i in range(26):
                if square[i][keyIndx] == char.lower():
                    plainIndx = i
                    break

            plainChar = square[0][plainIndx]
            #key = plainChar
            plaintext += plainChar.upper() if char.isupper() else plainChar
        #Punctuation
        else:
            plaintext += char

    return plaintext


#-------------------------------------
#Q2: Vigenere Crytanalysis Utilities #
#-------------------------------------

#-----------------------------------------------------------------------------
# Parameters:   text (string)
#               size (int)
# Return:       list of strings
# Description:  Break a given string into strings of given size
#               Result is provided in a list
#------------------------------------------------------------------------------
def text_to_blocks(text,size):
    # your code here
    blocks = []
    i=0
    while i < len(text):
        blocks.append(text[i:i+size])
        i += size

    return blocks

#-----------------------------------
# Parameters:   text (string)
# Return:       modifiedText (string)
# Description:  Removes all non-alpha characters from the given string
#               Returns a string of only alpha characters upper case
#-----------------------------------
def remove_nonalpha(text):
    # your code here
    modifiedText = ''
    for char in text:
        if char.isalpha():
            modifiedText += char

    return modifiedText

#-------------------------------------------------------------------------------------
# Parameters:   blocks: list of strings
# Return:       baskets: list of strings
# Description:  Assume all blocks have same size = n (other than last block)
#               Create n baskets
#               In basket[i] put character #i from each block
#---------------------------------------------------------------------------------------
def blocks_to_baskets(blocks):
    # your code here
    baskets = []

    size = len(blocks[0])

    for i in range(size):
        basket = ''

        for block in blocks:
            if len(block) > i: #If last block is shorter
                basket += block[i]

        baskets.append(basket)

    return baskets

#----------------------------------------------------------------
# Parameters:   ciphertext(string)
# Return:       I (float): Index of Coincidence
# Description:  Computes and returns the index of coincidence 
#               for a given text
#----------------------------------------------------------------
def get_indexOfCoin(ciphertext):
    # your code here
    ciphertext = remove_nonalpha(ciphertext)

    if len(ciphertext) == 0:
        return 0
        
    ciphertext = ciphertext.lower()
    
    alphaArray = [0]*26
    alphaString = utilities_A2.get_lower()

    for i in range(26):
        alphaArray[i] += ciphertext.count(alphaString[i])
    I = 0.00
    # for char in ciphertext:
    #     newchar = char.lower()
    #     charindex = newchar.index(alphaString)
    #     alphaArray[charindex] += 1
        
    for j in range(26):
        #I += (alphaArray[j] * (alphaArray[j] - 1))
        I += ((alphaArray[j]/len(ciphertext)) * ((alphaArray[j]-1)/(len(ciphertext)-1)))
    #I = I/(len(ciphertext) * (len(ciphertext) - 1))
    #I = I*26

    return I

#----------------------------------------------------------------
# Parameters:   ciphertext(string)
# Return:       key length (int)
# Description:  Uses Friedman's test to compute key length
#               returns key length rounded to nearest integer
#---------------------------------------------------------------
def getKeyL_friedman(ciphertext):
    # your code here

    k = (0.0265*len(ciphertext))/((0.065-get_indexOfCoin(ciphertext)) + (len(ciphertext)*(get_indexOfCoin(ciphertext)-0.0385)))
    k = int(round(k))

    return k

#----------------------------------------------------------------
# Parameters:   ciphertext(string)
# Return:       key length (int)
# Description:  Uses the Ciphertext Shift method to compute key length
#               Attempts key lengths 1 to 20
#---------------------------------------------------------------
def getKeyL_shift(ciphertext):
    #XBCRODWAATBMBFPGGCFWRMWCBPRXUPFJSBNMJAMZHERFTRCJJHNHWGUZCAYCVOJESYRUEKPPXPJJG
    #GCFWRMWCBPRXUPFJSBNMJAMZHERFTRCJJHNHWGUZCAYCVOJESYRUEKPPXPJJGXBCRODWAATBMBFPG
    
    maxMatch = 0
    shiftedText = ciphertext
    for i in range(20):
        matchNum = 0
        shiftedText = utilities_A2.shift_string(shiftedText, 1, 'l')
        
        for j in range(len(ciphertext)-i):
            
            #Check if characters match starting at char i
            if (ciphertext[j] == shiftedText[j]):
                matchNum += 1
        
        if matchNum > maxMatch:
            maxMatch = matchNum
            k = i+1

    return k


#---------------------------------
#   Q3:  Block Rotate Cipher     #
#---------------------------------
#-----------------------------------------------------------
# Parameters:   key (b,r)
# Return:       updatedKey (b, r)
# Description:  Assumes given key is in the format of (b(int),r(int))
#               Updates the key in three scenarios:
#               1- The key is too big (use modulo)
#               2- The key is negative
#               if an invalid key is given print error message and return (0,0)
#-----------------------------------------------------------
def adjustKey_blockRotate(key):
    # your code here
    if not isinstance(key, tuple) or len(key) != 2 or key[0] <= 0 or not isinstance(key[0], int) or not isinstance(key[1], int):
        print("Error (adjustKey_blockRotate): Invalid key", end='')
        updatedKey = (0, 0)
        return updatedKey

    newR = key[1]
    #If r is negative
    if key[1] < 0:
        newR = key[1] + key[0]
        while newR < 0:
            newR += key[0]
    
        #If r > b
        if (abs(key[1]) >= key[0]):
            newR = key[1] % key[0]
    
    #If r is positive
    else:
        #If r > b
        if (abs(key[1]) >= key[0]):
            newR = key[1] % key[0]
    
    updatedKey = (key[0], newR)

    return updatedKey

#-----------------------------------
# Parameters:   text (string)
# Return:       nonalphaList (2D List)
# Description:  Analyzes a given string
#               Returns a list of non-alpha characters along with their positions
#               Format: [[char1, pos1],[char2,post2],...]
#               Example: get_nonalpha('I have 3 cents.') -->
#                   [[' ', 1], [' ', 6], ['3', 7], [' ', 8], ['.', 14]]
#-----------------------------------
def get_nonalpha(text):
    # your code here
    nonalphaList = []
    for i in range(len(text)):
        if not text[i].isalpha():
            nonalphaList.append([text[i], i])

    return nonalphaList

#-----------------------------------
# Parameters:   text (str)
#               2D list: [[char1,pos1], [char2,pos2],...]
# Return:       modifiedText (string)
# Description:  inserts a list of nonalpha characters in the positions
#-----------------------------------
def insert_nonalpha(text, nonAlpha):
    # your code here
    if len(nonAlpha) == 0:
        return text
    texti = 0
    arrayi = 0
    modifiedText = ''
    for i in range(len(text)+len(nonAlpha)):
        if arrayi < len(nonAlpha) and (i == nonAlpha[arrayi][1] or texti == len(text)):
            modifiedText += nonAlpha[arrayi][0]
            arrayi += 1
        
        else:
            modifiedText += text[texti]
            texti += 1
    

    return modifiedText

#-----------------------------------------------------------
# Parameters:   plaintext (string)
#               key (b,r): (int,int)
# Return:       ciphertext (string)
# Description:  break plaintext into blocks of size b
#               rotate each block r times to the left
#-----------------------------------------------------------
def e_blockRotate(plaintext,key):
    # your code here

    #Preprocessing of key and text
    key = adjustKey_blockRotate(key)
    punctArray = get_nonalpha(plaintext)

    #Get alphabet characters only
    ciphertext = ''
    for char in plaintext:
        if char.isalpha():
            ciphertext +=  char

    #Pad the text
    pad = len(ciphertext) % key[0]
    for i in range(pad):
        ciphertext += 'q'

    #Encryption
    cipherArray = text_to_blocks(ciphertext, key[0])
    for i in range(len(cipherArray)):
        cipherArray[i] = utilities_A2.shift_string(cipherArray[i], key[1], 'l')

    #Convert back to string
    ciphertext = ''
    for block in cipherArray:
        ciphertext += block

    #Insert punctuation
    ciphertext = insert_nonalpha(ciphertext, punctArray)

    return ciphertext

#-----------------------------------------------------------
# Parameters:   ciphertext (string)
#               key (b,r): (int,int)
# Return:       plaintext (string)
# Description:  Decryption using Block Rotate Cipher
#-----------------------------------------------------------
def d_blockRotate(ciphertext,key):
    # your code here
    #Preprocessing of key and text
    key = adjustKey_blockRotate(key)
    punctArray = get_nonalpha(ciphertext)

    #Get alphabet characters only
    plaintext = ''
    for char in ciphertext:
        if char.isalpha():
            plaintext +=  char

    #Decryption
    plainTextArray = text_to_blocks(plaintext, key[0])
    for i in range(len(plainTextArray)):
        plainTextArray[i] = utilities_A2.shift_string(plainTextArray[i], key[1], 'r')

    #Convert back to string
    plaintext = ''
    for block in plainTextArray:
        plaintext += block

    #Remove padding
    while plaintext[-1] == 'q':
        plaintext = plaintext[:-1]

    #Insert punctuation
    plaintext = insert_nonalpha(plaintext, punctArray)

    return plaintext

#-----------------------------------------------------------
# Parameters:   ciphertext (string)
#               b1 (int): starting block size
#               b2 (int): end block size
# Return:       plaintext,key
# Description:  Cryptanalysis of Block Rotate Cipher
#               Returns plaintext and key (r,b)
#               Attempts block sizes from b1 to b2 (inclusive)
#               Prints number of attempts
#-----------------------------------------------------------
def cryptanalysis_blockRotate(ciphertext,b1,b2):
    # your code here
    attempt = 0
    plaintext = ""
    key = (0, 0)
    while b1 != b2:
        for i in range(1, b1):
            testText = d_blockRotate(ciphertext, (b1, i))
            attempt += 1
            
            if utilities_A2.is_plaintext(testText, "engmix.txt", 0.8):
                plaintext = testText
                key = (b1, i)
                break

        if plaintext != "":
            break
        
        b1 += 1

    if plaintext =="":
        print("Block Rotate Crypanalysis Failed. No key was found.")
    else:
        print("Key found after ", attempt, " attempts")
        print("Key = ", key)
        print("Plaintext: ", plaintext)

    return plaintext,key

#---------------------------------
#       Q4: Cipher Detector     #
#---------------------------------
#-----------------------------------------------------------
# Parameters:   ciphertext (string)
# Return:       cipherType (string)
# Description:  Detects the type of a given ciphertext
#               Categories: "Atbash Cipher, Spartan Scytale Cipher,
#                   Polybius Square Cipher, Shfit Cipher, Vigenere Cipher
#                   All other ciphers are classified as Unknown. 
#               If the given ciphertext is empty return 'Empty Ciphertext'
#-----------------------------------------------------------
def get_cipherType(ciphertext):
    # your code here
    cipherType = "Unknown"
    

    if ciphertext == "":
        cipherType = "Empty Ciphertext"

    if ciphertext == "Unknown":
        if utilities_A2.is_plaintext(ciphertext, "engmix.txt", 0.8):
            return "Unknown"

    if cipherType == "Unknown":

        #Index of coincidence
        iofc = get_indexOfCoin(ciphertext)

        #Inverse Chi Value
        text = ciphertext[:40]
        freqTable = utilities_A2.get_freqTable()
        freqTable = list(reversed(freqTable))

        charCount = utilities_A2.get_charCount(text)

        result = 0
        for i in range(26):
            Ci = charCount[i]
            Ei = freqTable[i]*len(text)
            result += ((Ci-Ei)**2)/Ei

        chi2 = result

        
        #Most common char
        tempText = remove_nonalpha(ciphertext)
        charArray = utilities_A2.get_charCount(tempText)
        comChar = charArray.index(max(charArray))

        if cipherType == "Unknown":
            poly = True

            for char in ciphertext:
                if char.isalpha():
                    poly = False

            if poly == True:
                cipherType = "Polybius Cipher"
                
    if cipherType == "Unknown":
        print(iofc)
        if (iofc >= 0.062 and iofc <= 0.068):
            if (comChar == 4):#e is most common char
                cipherType = "Spartan Scytale Cipher"
            elif (chi2 < 150):        
                cipherType = "Atbash Cipher"
            else:
                cipherType  = "Shift Cipher"
        #               0.0355                      0.0415          
        elif iofc >= (0.0385 - 0.03) and iofc <= (0.0385 + 0.03):
            cipherType = "Vigenere Cipher"

            # if iofc >= 0.0355 or iofc <= 0.0415:
            #      #Random text - Vigenere Cipher
            #     cipherType = "Vigenere Cipher"



    return cipherType

#-------------------------------------
#  Q5: Wheastone Playfair Cipher     #
#-------------------------------------
#-----------------------------------------------------------
# Parameters:   plaintext (string)
# Return:       modifiedPlain (string)
# Description:  Modify a plaintext through the following criteria
#               1- All non-alpha characters are removed
#               2- Every 'W' is translsated into 'VV' double V
#               3- Convert every double character ## to #X
#               4- if the length of text is odd, add X
#               5- Output is formatted as pairs, separated by space
#                   all upper case
#-----------------------------------------------------------
def formatInput_playfair(plaintext):
    # your code here
    plaintext = remove_nonalpha(plaintext)
    plaintext = plaintext.upper()
    plaintext = plaintext.replace("W", "VV")
    if len(plaintext) % 2 == 1:
        plaintext += "X"

    #Replace double letters with #X
    i=0
    while i < len(plaintext):
        if plaintext[i] == plaintext[i+1]:
            tempStr = plaintext[i+1:]
            plaintext = plaintext[:i+1] + "X" 
            if len(tempStr) > 1:
                plaintext += tempStr[1:]
        i+=2

    #Add spaces
    i=0
    modifiedPlain = ''
    while i < len(plaintext):
        modifiedPlain += plaintext[i]
        modifiedPlain +=  plaintext[i+1]
        modifiedPlain += " "
        i+=2

    return modifiedPlain

#-------------------------------------------------------------------------------------
# Parameters:   plaintext(string)
#               key: playfair Square (2D List)
# Return:       ciphertext (string)
# Description:  Encryption using Wheatstone Playfair Cipher
#---------------------------------------------------------------------------------------
def e_playfair(plaintext, key):
    # your code here

    plaintext = formatInput_playfair(plaintext)
    ciphertext = ''

    charI=0
    while charI < len(plaintext):
        char1 = [0, 0]
        char2 = [0, 0]

        for i in range(len(key)):
            for j in range(len(key[0])):

                if key[i][j] == plaintext[charI]:
                    char1 = [i, j]

                if key[i][j] == plaintext[charI+1]:
                    char2 = [i, j]

        #Same row
        if (char1[1] == char2[1]):
            #Wraparound char1
            if char1[0] == len(key)-1:
                ciphertext += key[0][char1[1]]
            #No wraparound
            else:
                ciphertext += key[char1[0]+1][char1[1]]

            #Wraparound char2
            if char2[0] == len(key)-1:
                ciphertext += key[0][char2[1]]
            #No wraparound
            else:
                ciphertext += key[char2[0]+1][char2[1]]
            
            ciphertext += " "
        
        #Same column    
        elif (char1[0] == char2[0]):
            #Wraparound char1
            if char1[1] == len(key)-1:
                ciphertext += key[char1[0]][0]
            else:
                ciphertext += key[char1[0]][char1[1]+1]

            if char2[1] == len(key)-1:
                ciphertext += key[char2[0]][0]
            else:
                ciphertext += key[char2[0]][char2[1]+1]
            
            ciphertext += " "

        else:
            ciphertext += key[char1[0]][char2[1]]
            ciphertext += key[char2[0]][char1[1]]
            ciphertext += " "

        charI += 3

    return ciphertext

#-------------------------------------------------------------------------------------
# Parameters:   plaintext(string)
#               key: playfair Square (2D List)
# Return:       ciphertext (string)
# Description:  Decryption using Wheatstone Playfair Cipher
#-------------------------------------------------------------------------------
def d_playfair(ciphertext, key):
    # your code here
    ciphertext = formatInput_playfair(ciphertext)
    plaintext = ''

    charI=0
    while charI < len(ciphertext):
        char1 = [0, 0]
        char2 = [0, 0]

        for i in range(len(key)):
            for j in range(len(key[0])):

                if key[i][j] == ciphertext[charI]:
                    char1 = [i, j]

                if key[i][j] == ciphertext[charI+1]:
                    char2 = [i, j]

        #Same row
        if (char1[1] == char2[1]):
            #Wraparound char1
            if char1[0] == 0:
                plaintext += key[len(key)-1][char1[1]]
            #No wraparound
            else:
                plaintext += key[char1[0]-1][char1[1]]

            #Wraparound char2
            if char2[0] == 0:
                plaintext += key[len(key)-1][char2[1]]
            #No wraparound
            else:
                plaintext += key[char2[0]-1][char2[1]]
            
            plaintext += " "
        
        #Same column    
        elif (char1[0] == char2[0]):
            #Wraparound char1
            if char1[1] == 0:
                plaintext += key[char1[0]][len(key)-1]
            else:
                plaintext += key[char1[0]][char1[1]-1]

            if char2[1] == 0:
                plaintext += key[char2[0]][len(key)-1]
            else:
                plaintext += key[char2[0]][char2[1]-1]
            
            plaintext += " "
            
        else:
            plaintext += key[char1[0]][char2[1]]
            plaintext += key[char2[0]][char1[1]]
            plaintext += " "

        charI += 3

    return plaintext
