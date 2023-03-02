#--------------------------
# Joseph Myc | 160 740 900
# CP460 (Fall 2019)
# Midterm Student Solution File
#--------------------------

#-----------------------------------------------
# Remember to change the name of the file to:
#               solution.py
# Delete this box after changing the file name
# ----------------------------------------------

#----------------------------------------------
# You can not add any library other than these:
import math
import string
import random
import utilities
#----------------------------------------------

#---------------------------------
#           Q0: Matching         #
#---------------------------------
#-------------------------------------------------------
#                   EDIT THIS FILE
# change this function such that it makes the proper matching
# Also provide your description of how you found the matching. 
#-------------------------------------------------------
def match_files():


    
    cipher1 = 'ciphertext_Joseph_Myc_q1.txt' 
    plain1  = 'plaintext_Joseph_Myc_q1.txt'  

    cipher2 = 'ciphertext_Joseph_Myc_q2.txt' 
    plain2  = 'plaintext_Joseph_Myc_q2.txt' 

    cipher3 = 'ciphertext_Joseph_Myc_q3.txt' 
    plain3  = 'plaintext_Joseph_Myc_q3.txt' 

    cipher4 = 'ciphertext_Joseph_Myc_q4.txt' 
    plain4  = 'plaintext_Joseph_Myc_q4.txt'  

    viI=-1
    subI=-1 
    shiftI=-1 
    cryptI=-1 

    cipherArray = [utilities.file_to_text(cipher1), utilities.file_to_text(cipher2), utilities.file_to_text(cipher3), utilities.file_to_text(cipher4)]

    for i in range(4):
        iOFc = utilities.get_indexOfCoin(cipherArray[i])
        #print("Index of coincidence for ", i, " is ", iOFc)

        #Most common char
        tempText = utilities.remove_nonalpha(cipherArray[i])
        charArray = utilities.get_charCount(tempText)
        comChar = charArray.index(max(charArray))
        #print("Most common char: ", comChar)

        #Vigenere
        if (iOFc > 0.0415 and iOFc < 0.062):
            if viI == -1:
                cipher1 = "ciphertext_Joseph_Myc_q" + str(i+1) + ".txt"
                plain1 = "plaintext_Joseph_Myc_q" + str(i+1) + ".txt"
                viI = i
            else:
                print("ERROR: multiple viginere ciphers found")
        
        elif (iOFc >= 0.062 and iOFc <= 0.068):
            if comChar == 4:
                if cryptI == -1:
                    cipher4 = "ciphertext_Joseph_Myc_q" + str(i+1) + ".txt"
                    plain4 = "plaintext_Joseph_Myc_q" + str(i+1) + ".txt"
                    cryptI = i
                else:
                    print("ERROR: multiple xCrypt ciphers found")
            
            #Substitution cipher
            else:
                if subI == -1:
                    cipher2 = "ciphertext_Joseph_Myc_q" + str(i+1) + ".txt"
                    plain2 = "plaintext_Joseph_Myc_q" + str(i+1) + ".txt"
                    subI = i
                else:
                    print("ERROR: multiple substitution ciphers found")
                

        #xShift cipher
        else:
            if shiftI == -1:
                    cipher3 = "ciphertext_Joseph_Myc_q" + str(i+1) + ".txt"
                    plain3 = "plaintext_Joseph_Myc_q" + str(i+1) + ".txt"
                    shiftI = i
            else:
                print("ERROR: multiple shift ciphers found")


    # Files related to vigenere cipher
    vigenereFiles = [plain1,cipher1]
    print('The Vigenere ciphertext file is:',cipher1)
    print('I found that the above file is a vigenere cipher by calculating that its index of coincidence is between the values for english and random text +/- 0.003.') 
    print()
    
    # Files related to substitution cipher
    
    subFiles = [plain2,cipher2]
    print('The Substitution ciphertext file is:',cipher2)
    print('I found that the above file is a substitution cipher by calculating that its index of coincidence is within the values for english +/- 0.03 but its most common character was not \'e\'')
    print()
    
    # Files related to xshift cipher
    xshiftFiles = [plain3,cipher3]
    print('The xshift ciphertext file is:',cipher3)
    print('I found that the above file is an xshift cipher by calculating that its index of coincidence was outside the range of both english +/- 0.03 and viginere (0.0415 - 0.062)') 
    print()
    
    # Files related to xcrypt cipher
    xcryptFiles = [plain4,cipher4]
    print('The xcrypt ciphertext file is:',cipher4)
    print('I found that the above file is an xcrypt cipher by calculating that its index of coincidence is within the values for english +/- 0.03 and its most common character was \'e\'') 
    print()
    
    return [vigenereFiles,subFiles,xshiftFiles,xcryptFiles]

#---------------------------------
#         Q1: Vigenere           #
#---------------------------------

#-----------------------------------------------------------
# Parameters:   plaintext(string)
#               key (str): a phrase
# Return:       ciphertext (string)
# Description:  Enryption using Vigenere Cipher (Q1)
#-----------------------------------------------------------
def e_vigenere(plaintext, key):
    square = utilities.get_vigenereSquare()

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

#-----------------------------------------------------------
# Parameters:   ciphertext(string)
#               key (str): a phrase
# Return:       ciphertext (string)
# Description:  Decryption using Vigenere Cipher (Q1)
#-----------------------------------------------------------
def d_vigenere(ciphertext, key):
    
    square = utilities.get_vigenereSquare()

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

#-----------------------------------------------------------
# Parameters:   ciphertext(string)
# Return:       key,plaintext
# Description:  Cryptanlysis of Vigenere Cipher (Q1)
#-----------------------------------------------------------
def cryptanalysis_vigenere(ciphertext):

    key = ""
    plaintext = ""

    #Find average IC value for blocks of size 1-20
    alphaCipher = utilities.remove_nonalpha(ciphertext)
    
    maxAvg = 0.00
    per = 0
    for i in range(20):
        blockArray = utilities.text_to_blocks(alphaCipher, i+1)
        basketArray = utilities.blocks_to_baskets(blockArray)
        avgIofC = 0

        for basket in basketArray:
            basketIofC = utilities.get_indexOfCoin(basket)
            avgIofC += basketIofC

        avgIofC = avgIofC / len(basketArray)
        if avgIofC > maxAvg:
            maxAvg = avgIofC
            per = i+1

        #print("Period:", (i+1), "\tAvg IC: ", avgIofC)

    #print("Most likely key length: ", per, " with value ", maxAvg)

    blockArray = utilities.text_to_blocks(alphaCipher, per)
    basketArray = utilities.blocks_to_baskets(blockArray)
    alphaArray = utilities.get_lower()

    minChi = utilities.get_chiSquared(basketArray[0])
    minI = 0
    for j in range(len(basketArray)):
        shiftKey, shiftText = utilities.cryptanalysis_shift(basketArray[j])
        key += alphaArray[shiftKey[0]]

    plaintext = d_vigenere(ciphertext, key)

    return key,plaintext

def comments_q1():
    print('Comments:')  
    print("""They key length was found by splitting the string into blocks of size 1-21, and then splitting those blocks into baskets.  The index of coincidence for each basket was then found, and an average index of coincidence was taken for that block size.  The block size with the highest average index of coincidence was considerd to be the most likely key length as it suggests that using this length creates an array of shift ciphers.  Block sizes with the next highest index of coincidence would have been considered if this size had failed.""")  
    print("""To find the keyword, i assume the found key length is correct, split the string into blocks, and then baskets, using this key length.  In each basket, all characters would be encrypted using the same key character, so I then perform a cryptanalysis of a shift cipher on each basket, by using chi squared to find the most likely character for each character in the key.  This is done by performing a shift decryption for each character in the alphabet, and taking the character for the shift decryption with the minimum found chi value""")     
    return

#---------------------------------
#   Q2: Substitution Cipher      #
#---------------------------------
#-------------------------------------------------------
# Parameters:   plaintext(str)
#               key: subString (str)
# Return:       ciphertext (string)
# Description:  Encryption using substitution (Q2)
#-------------------------------------------------------
def e_substitution(plaintext,key):
    ciphertext = ""
    baseKey = utilities.get_baseString()
    if '#' not in key:
        key = utilities.adjust_key(key)
    plaintext = plaintext.replace('\n', '#')
    
    for char in plaintext:
        if char.isalpha() and (char.lower() in baseKey) and char.isupper():
            ciphertext +=  key[baseKey.index(char.lower())].upper()
        elif char.lower() in baseKey:
            ciphertext += key[baseKey.index(char)]
        else: 
            ciphertext += char
    
    ciphertext = ciphertext.replace('#', '\n')

    return ciphertext

#-----------------------------------------
# Parametes:    ciphertext (str)
#               key: subString (str)
# Return:       plaintext (str)
# Description:  Decryption using substitution (Q2)
#-----------------------------------------
def d_substitution(ciphertext,key):
    plaintext = ""
    baseKey = utilities.get_baseString()
    if '#' not in key:
        key = utilities.adjust_key(key)
    ciphertext = ciphertext.replace('\n', '#')
    
    for char in ciphertext:
        if char.isalpha() and (char.lower() in baseKey) and char.isupper():
            plaintext +=  baseKey[key.index(char.lower())].upper()
        
        elif char.lower() in baseKey:
            plaintext += baseKey[key.index(char)]
            
        #Special character not in baseKey
        else: 
            plaintext += char
    
    plaintext = plaintext.replace('#', '\n')

    return plaintext

def cryptanalysis_substitution(ciphertext):#. , ;   # " ? ' ! : -
        #    abcdefghijklmnopqrstuvwxyz.,; #"?'!:-
    key = '''dnxqhkejzgpyvcaiwrsufmbolt, :;?!'"#.-'''   #<--- change this line with your key
    
    plaintext = d_substitution(ciphertext,key)

    # baseString = utilities.get_baseString()
    # baseString = utilities.adjust_key(baseString)
    # utilities.debug_substitution(ciphertext, baseString)
    
    key = utilities.adjust_key(key)                     #<--- keep this line
    return key,plaintext

def comments_q2():
    print('Comments:')
    print('See Joseph_Myc_sub_log.txt file') #<----- edit this
    return

#---------------------------------
#           Q3: Xshift           #
#---------------------------------

#-----------------------------------------
# Parametes:    plaintext (str)
#               key: (shiftString,shifts)
# Return:       ciphertext (str)
# Description:  Encryption using Xshift Cipher
#-----------------------------------------
def e_xshift(plaintext, key):
    ciphertext = ""
    for char in plaintext:
        if char.isalpha():
            charI = key[0].index(char)
            charI = (charI + key[1]) % 52
            ciphertext += key[0][charI]
        else:
            ciphertext += char
    
    return ciphertext

#-----------------------------------------
# Parametes:    ciphertext (str)
#               key: (shiftString,shifts)
# Return:       plaintext (str)
# Description:  Decryption using Xshift Cipher
#-----------------------------------------
def d_xshift(ciphertext, key):

    plaintext = ""
    for char in ciphertext:
        if char.isalpha():
            charI = key[0].index(char)
            charI = (charI - key[1])
            while charI < 0:
                charI += 52

            plaintext += key[0][charI]
        else:
            plaintext += char

    return plaintext

#-----------------------------------------
# Parametes:    ciphertext (str)
# Return:       key,plaintext
# Description:  Cryptanalysis of  Xshift Cipher
#-----------------------------------------
def cryptanalysis_xshift(ciphertext):
    
    key = ("", 0)
    plaintext = ""
    upperCipher = ""
    lowerCipher = ""
    alphaText = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    lowAlpha = "abcdefghijklmnopqrstuvwxyz"
    upAlpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    alphaCountArray = [0]*52

    #Count each char in ciphertext (upper and lower seperately)
    for char in ciphertext:
        if char.isalpha():
            chari = alphaText.index(char)
            alphaCountArray[chari] += 1

    #Get index of 2 most common chars in ciphertext (which will be translated from e and t)
    ei = 0
    ti = 0
    for num in range(len(alphaCountArray)):
        if alphaCountArray[num] > alphaCountArray[ei]:
            ti = ei
            ei = num

    echar = alphaText[ei]
    tchar = alphaText[ti]    

    foundKey = False
    #Both remained lower case
    if ei < 26 and ti < 26:
        #Lowercase atbash, possible key is 0->6 or (21+26)->52 
        if ei > ti:
            kStrArray = [(lowAlpha[::-1] + upAlpha), (lowAlpha[::-1] + upAlpha[::-1]), (upAlpha + lowAlpha[::-1]), (upAlpha[::-1] + lowAlpha[::-1])]
            
            for kStr in kStrArray:
                for i in range(52):

                    plaintext = d_xshift(ciphertext, (kStr, i))
                    if (utilities.is_plaintext(plaintext, "engmix.txt", 0.9)):
                        key = (kStr, i)
                        break
                
                if key[0] != "":
                    break

        #Lowercase normal
        else:
            kStrArray = [(lowAlpha + upAlpha), (lowAlpha + upAlpha[::-1]), (upAlpha + lowAlpha), (upAlpha[::-1] + lowAlpha)]
            
            for kStr in kStrArray:
                for i in range(52):

                    plaintext = d_xshift(ciphertext, (kStr, i))
                    if (utilities.is_plaintext(plaintext, "engmix.txt", 0.9)):
                        key = (kStr, i)
                        break
                
                if key[0] != "":
                    break

    #Both translated to upper case
    elif ei >=26 and ti >= 26:
        #Uppercase atbash
        if ei > ti:
            kStrArray = [(lowAlpha + upAlpha[::-1]), (lowAlpha[::-1] + upAlpha[::-1]), (upAlpha[::-1] + lowAlpha), (upAlpha[::-1] + lowAlpha[::-1])]
            
            for kStr in kStrArray:
                for i in range(52):

                    plaintext = d_xshift(ciphertext, (kStr, i))
                    if (utilities.is_plaintext(plaintext, "engmix.txt", 0.9)):
                        key = (kStr, i)
                        break
                
                if key[0] != "":
                    break

        #Uppercase normal
        else:
            kStrArray = [(lowAlpha + upAlpha), (lowAlpha[::-1] + upAlpha), (upAlpha + lowAlpha), (upAlpha + lowAlpha[::-1])]
            
            for kStr in kStrArray:
                for i in range(52):

                    plaintext = d_xshift(ciphertext, (kStr, i))
                    if (utilities.is_plaintext(plaintext, "engmix.txt", 0.9)):
                        key = (kStr, i)
                        break
                
                if key[0] != "":
                    break
                                    #     21            47
    #e remained lowercase only -> key <= (26-5) or > (26-5)+26 but < 52
    elif ei < 26:
        kStrArray = [(lowAlpha + upAlpha[::-1]), (lowAlpha[::-1] + upAlpha[::-1]), (upAlpha[::-1] + lowAlpha), (upAlpha[::-1] + lowAlpha[::-1]), (lowAlpha + upAlpha), (lowAlpha[::-1] + upAlpha), (upAlpha + lowAlpha), (upAlpha + lowAlpha[::-1])]
        
        for kStr in kStrArray:
            i = 0

            while i < 52:

                plaintext = d_xshift(ciphertext, (kStr, i))
                if (utilities.is_plaintext(plaintext, "engmix.txt", 0.9)):
                    key = (kStr, i)
                    break

                #index increment
                if i == 21:
                    i += 26
                else:
                    i += 1
            
            if key[0] != "":
                break
        

    #t remained lower case only -> key <= (26-20) or > (26-20)+26 but < 52
    else:
        kStrArray = [(lowAlpha + upAlpha[::-1]), (lowAlpha[::-1] + upAlpha[::-1]), (upAlpha[::-1] + lowAlpha), (upAlpha[::-1] + lowAlpha[::-1]), (lowAlpha + upAlpha), (lowAlpha[::-1] + upAlpha), (upAlpha + lowAlpha), (upAlpha + lowAlpha[::-1])]
            
        for kStr in kStrArray:
            i = 0
            while i < 52:

                plaintext = d_xshift(ciphertext, (kStr, i))
                if (utilities.is_plaintext(plaintext, "engmix.txt", 0.9)):
                    key = (kStr, i)
                    break

                #index increment
                if i == 6:
                    i += 26
                else:
                    i += 1
            
            if key[0] != "":
                break

    #Atupper, Atlower
    #Upper, Lower
    #Atupper, Lower
    #Upper, Atlower
    #Atlower, Atupper
    #Lower, Upper 
    #Lower, Atupper 
    #Atlower, Upper 

    return key,plaintext

def comments_q3():
    print('Comments:')
    print('''Brute-force space is: half of the total state space of eight possible keystrings:
Atupper, Atlower
Upper, Lower
Atupper, Lower
Upper, Atlower
Atlower, Atupper
Lower, Upper 
Lower, Atupper 
Atlower, Upper, 
and 52 possible keynums:a-z + A-Z''')               
    print('''I find the 2 most common characters in the ciphertext and assume they translate from e and t (2 most common characters in english.
I can then use the position of the translated characters to reduce the state space.
If both characters are still lowercase after the encryption, i can tell if the lowercase part of the keystring is atbash by the order the encrypted characters are in, reducing the search of keystrings from 8 to 4.
If both characters are now uppercase after then encryption, i can tell if the uppercase part of the keystring is atbash by the order of the encrypted characters, reducing the search of keystrings from 8 to 4.
If one character is lowercase and one is uppercase after the encryption, i can reduce the search for the index by half by only searching shifts possible for e or t that would keep them lowercase.  This makes the search index 26 long instead of 52.)''')  
    return

#---------------------------------
#           Q4: Xcrypt           #
#---------------------------------
#-------------------------------------------------------
# Parameters:   plaintext(string)
#               key (int)
# Return:       ciphertext (string)
# Description:  Encryption using xcrypt (Q4)
#-------------------------------------------------------
def e_xcrypt(plaintext,key):
    
    ciphertext = ""

    fill = len(plaintext) % key
    for i in range(key - fill):
        plaintext += 'q'


    blockArray = utilities.text_to_blocks(plaintext, key)
    basketArray = utilities.blocks_to_baskets(blockArray)

    for item in basketArray:
        ciphertext += item

    return ciphertext

#-------------------------------------------------------
# Parameters:   ciphertext(string)
#               key (int)
# Return:       plaintext (string)
# Description:  Decryption using xcrypt (Q4)
#-------------------------------------------------------
def d_xcrypt(ciphertext,key):
    
    plaintext = ""

    width = int(math.ceil(len(ciphertext)/key))

    fill = len(ciphertext) % key
    for i in range(fill):
        ciphertext += 'q'

    solveArray =  utilities.new_matrix(width,key,"")
    count = 0
    for i in range(key):
        for j in range(width):
            solveArray[j][i] = ciphertext[count]
            count += 1

    for i in range(width):
        for j in range(key):
            plaintext += solveArray[i][j]

    while plaintext[-1] == 'q':
        plaintext = plaintext[:-1]
    
    return plaintext

#-------------------------------------------------------
# Parameters:   ciphertext(string)
# Return:       key (int),plaintext (str)
# Description:  cryptanalysis of xcrypt (Q4)
#-------------------------------------------------------
def cryptanalysis_xcrypt(ciphertext):
    plaintext = ""
    key = 0
    for i in range(1, 501):
        if (len(ciphertext) % i) == 0:
            plaintext = d_xcrypt(ciphertext, i)
            if (utilities.is_plaintext(plaintext, "engmix.txt", 0.9)):
                break

    key = i

    return key,plaintext

#-------------------------------------------------------
# Parameters:   None
# Return:       None
# Description:  Your comments on Q4 solution
#-------------------------------------------------------
def comments_q4():
    print('My Comments:')
    print('Used threshold is: ',0.9)              # <---- edit this
    print('Cryptanalysis Method: Loop through possible keys.  Check if ciphertext fits in table block using the current key by checking the cipher text length % key.  If it fits, attempt decryption with the key and check that the output is english plaintext with a threshold of 0.9.')    # <---- edit this
    return
