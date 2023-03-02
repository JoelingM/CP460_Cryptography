#--------------------------
# CP460 (Fall 2019)
# Final Exam
# your name <----------------------
# your student ID <----------------
#--------------------------

import math
import string
import mod
import SDES
import utilities
import q4

#---------------------------------
#           Honor Pledge         #
#---------------------------------

def honor_pledge():
    print('I certify that I have completed this final exam independently, without seeking any external help online or offline\nThe way i have solved this final exam reflects my moral values and ethical standards.\nI understand that plagiarism results in failing the course and potential suspention from the program') 
    return 
#---------------------------------
#       Q1: mathCipher          #
#---------------------------------

def isValidKey_mathCipher(key):
    #Check overall key
    if not isinstance(key, tuple) or len(key) != 2:
        return False

    #Check substring
    if not isinstance(key[0], str) or len(key[0]) < 2:
        return False

    #Check k
    if not isinstance(key[1], list) or len(key[1]) != 3 or not isinstance(key[1][0], int) or not isinstance(key[1][1], int) or not isinstance(key[1][2], int):
        return False
    
    m = len(key[0])
    # print(m)
    # print(mod.has_mul_inv(key[1][0], m))
    # print(mod.has_mul_inv(key[1][1], m))
    # print(mod.has_mul_inv(key[1][2], m))
    if mod.has_mul_inv(key[1][0], m) and mod.has_mul_inv(key[1][1], m):
        return True

    return False
    
def e_mathCipher(plaintext, key):
    if not isinstance(plaintext, str) or plaintext == '':
        print('Error(e_mathCipher): invalid plaintext', end='')
        return

    if not isValidKey_mathCipher(key):
        print('Error(e_mathCipher): Invalid key', end = '')
        return
    
    ciphertext = ''
    for char in plaintext:
        if char.lower() in key[0].lower():
            num = key[0].lower().index(char.lower())
            y = (key[1][1] * ((key[1][0] * num) + key[1][1])) - key[1][2]
            y = y % len(key[0])

            if char.isupper():
                ciphertext = ciphertext + key[0][y].upper()
            else:
                ciphertext = ciphertext + key[0][y].lower()

        else:
            ciphertext = ciphertext + char

    return ciphertext

def d_mathCipher(ciphertext,key):
    if not isinstance(ciphertext, str) or ciphertext == '':
        print('Error(d_mathCipher): invalid ciphertext', end='')
        return

    if not isValidKey_mathCipher(key):
        print('Error(d_mathCipher): Invalid key', end = '')
        return
    
    plaintext = ''
    m = len(key[0])
    a = mod.mul_inv(key[1][0], m)
    b = mod.mul_inv(key[1][1], m)

    for char in ciphertext:
        if char.lower() in key[0].lower():
            num = key[0].lower().index(char.lower())
            y = (((num + key[1][2]) * b) - key[1][1]) * a
            y = y % len(key[0])

            if char.isupper():
                plaintext = plaintext + key[0][y].upper()
            else:
                plaintext = plaintext + key[0][y].lower()
                
        else:
            plaintext = plaintext + char

    return plaintext

def analyze_mathCipher(baseString):
    m = len(baseString)
    total = m ** 3
    valid = total
    illegal = 0
    noCipher = 0
    decimation = 0
    decFlag = True
    for a in range(1, m+1):
        for b in range(1, m+1):
            for c in range(1, m+1):
                decFlag = True
                #Illegal
                if not mod.has_mul_inv(a, m) or not mod.has_mul_inv(b, m):
                    illegal += 1
                    decFlag = False

                #No Cipher
                if ((b*a) == 1 or (b*a)%m == 1) and ((b**2) - c) % m == 0:
                    noCipher += 1
                    decFlag = False

                #Decimation
                if decFlag == True and ((b**2) - c) % m == 0:
                    decimation += 1
                    valid -= 1
                elif decFlag == False:
                    valid -= 1
    
    return [total,illegal,noCipher,decimation,valid]

def stats_mathCipher():
    primes = []
    with open('primes.txt', 'r') as f:
        text = f.read()
    for line in text.split():
        if int(line) <= 100:
            primes.append(int(line))

    m = 'aa'
    avg = -1.00
    best = -1.00
    worst = -1.00
    pavg = -1.00
    pbest = -1.00
    pworst = -1.00
    npavg = -1.00
    npbest = -1.00
    npworst = -1.00
    p = 0
    np = 0

    
    for i in range(2, 101):
        results = analyze_mathCipher(m)

        #All numbers
        if avg == -1:
            avg = results[4]/results[0]
            best = results[4]/results[0]
            worst = results[4]/results[0]
        else:
            avg += results[4]/results[0]
            if results[4]/results[0] > best:
                best = results[4]/results[0]
            if results[4]/results[0] < worst:
                worst = results[4]/results[0]

        #Primes
        if i in primes:
            if pavg == -1:
                pavg = results[4]/results[0]
                pbest = results[4]/results[0]
                pworst = results[4]/results[0]
            else:
                pavg += results[4]/results[0]
                if results[4]/results[0] > pbest:
                    pbest = results[4]/results[0]
                if results[4]/results[0] < pworst:
                    pworst = results[4]/results[0]
            p += 1

        #Non primes
        else:
            if npavg == -1:
                npavg = results[4]/results[0]
                npbest = results[4]/results[0]
                npworst = results[4]/results[0]
            else:
                npavg += results[4]/results[0]
                if results[4]/results[0] > npbest:
                    npbest = results[4]/results[0]
                if results[4]/results[0] < npworst:
                    npworst = results[4]/results[0]
            np += 1

        m += 'a'

    avg = (avg/99)
    pavg = (pavg/p)
    npavg = (npavg/np) 

    print('For all numbers:')
    print('\tAverage = {0:.2f}%'.format(avg*100)) #<----- edit these
    print('\tBest = {0:.2f}%'.format(worst*100))
    print('\tWorst = {0:.2f}%'.format(best*100))
    print('For Primes:')
    print('\tAverage = {0:.2f}%'.format(pavg*100))
    print('\tBest = {0:.2f}%'.format(pworst*100))
    print('\tWorst = {0:.2f}%'.format(pbest*100))
    print('For non Primes:')
    print('\tAverage = {0:.2f}%'.format(npavg*100))
    print('\tBest = {0:.2f}%'.format(npworst*100))
    print('\tWorst = {0:.2f}%'.format(npbest*100))
    return
                            
def cryptanalysis_mathCipher(ciphertext):
    baseStr = utilities.get_baseString()
    counter = 0
    dictList = utilities.load_dictionary("engmix.txt")
    foundFlag = False
    for i in range(26, len(baseStr)):
        subStr = baseStr[:i]
        m = len(subStr)
        for a in range(1, m+1):
            for b in range(1, m+1):
                for c in range(1, m+1):
                    key = (subStr, [a, b, c])
                    #Invalid
                    if not mod.has_mul_inv(a, m) or not mod.has_mul_inv(b, m) or (((b*a) == 1 or (b*a)%m == 1) and ((b**2) - c) % m == 0) or ((b**2) - c) % m == 0:
                        #print("Invalid at", key)
                        continue

                    counter += 1
                    plaintext = d_mathCipher(ciphertext,key)
                    if utilities.is_plaintext(plaintext, dictList, 0.9):
                        foundFlag = True
                        break

                if foundFlag:
                    break
            if foundFlag:
                break
        if foundFlag:
            break
    if foundFlag:
        print("key found after ", counter, 'attempts')
    return plaintext,key
    
#---------------------------------
# Q2: Myszkowski Cryptanalysis   #
#---------------------------------

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
        print("Error: Invalid Myszkowski Key ", end='')
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

def q2_description1():
    print('Cryptanalysis Strategy (Brute Force 3 characters): ')
    print('Only checks a key if it has both repeat characters and a unique character.  This excludes all cases where letters are all the same, and where all letters are different.') #<------------ change this line
    print('Worst Case Scenario: 1950') #<-------- change X
    print()
    return

def q2_description2():
    print('Cryptanalysis Strategy (Dictionary Attack): ')
    print('Put the dictionary into a sorted array.  Then use a binary search to find the index of the first word in the array with the known length n.  Then, loop through the words of length n until a solution is found or words are no longer of length n.  For each word, checks that the word is a valid key possibility (duplicate and unique characters) before testing it using decryption and is_plaintext.') #<------------ change this line
    print('Worst Case Scenario: 10805 attempts.  The longest set of strings was found to be 13311 with length 8, but of those strings only 10513 were valid.  However, length 9 had 10805 valid strings.  Therefore this is the worst case scenerio.')
    print()
    return

def q2_description3():
    print('Cryptanalysis Strategy (5-Triple): ')
    print('''Key has 1 repeated letter and 2 unique letters.
    Key order will be 1 of 3 scenerios: 
    assuming c is repeated:
    a, b ->both unique are before repeated 
    a, d ->One is before repeated and one is after
    d, e ->Both are after repeated
    Therefore check all permutations of these possibilities
    abccc, 
    acbcc, cabcc, 
    accbc, cacbc, ccabc, 
    acccb, caccb, ccacb, cccab
    baccc, 
    bcacc, cbacc, 
    bccac, cbcac, ccbac, 
    bccca, cbcca, ccbca, cccba
    20 permutations for 3 scenerios = 60 possibilities''') #<------------ change this line
    print('Dictionary returned 1939 valid key words.  However, many of these words will result in the same key, which is why this key space is larger.') #<------------ change this line
    print('Brute force is better than dictionary.  60 vs 1939 worst case.') #<------------ change this line
    print()
    return

def cryptanalysis1_myszkowski(ciphertext):
    alpha = utilities.get_lower()
    m = len(ciphertext)
    dictList = utilities.load_dictionary("engmix.txt")
    count = 0
    key = ''
    foundFlag = False
    #at least one dublicate, at least 1 unique
    for i in range(26):
        for j in range(26):
            for k in range(26):
                dupFlag = False
                unFlag = False
                if i==j or i==k or j==k:
                    dupFlag = True
                if (i != j and i != k) or (j != i and j != k) or (k != i and k != j):
                    unFlag = True

                if dupFlag and unFlag:
                    count += 1
                    key = alpha[i] + alpha[j] + alpha[k]
                    plaintext = d_myszkowski(ciphertext,key)
                    if utilities.is_plaintext(plaintext, dictList, 0.9):
                        foundFlag = True
                        break
            if foundFlag:
                break
        if foundFlag:
            break
    if foundFlag:
        print("key found after ", count, 'attempts')
        return plaintext,key
    return 'Failed', ''

def cryptanalysis2_myszkowski(ciphertext,length):  
    count = 0
    alpha = utilities.get_lower()
    dictList = utilities.load_dictionary("engmix.txt")

    with open('engmix.txt', 'r', encoding=" ISO-8859-15") as f:
        dictList2 = f.read().split()
    
    # #Check worst case scenario
    # words = [0]*40
    # validCount = 0
    # for word in dictList2:
        
    #     #Validate word
    #     chars = [0]*26
    #     unique = False
    #     duplicate = False
    #     #Count number of each character
    #     for char in word:
    #         if char.isalpha():
    #             chars[alpha.index(char)] += 1

    #     for num in chars:
    #         if num == 1:
    #             unique = True
    #         if num > 1:
    #             duplicate = True
    #     if unique and duplicate:
    #         words[len(word)] += 1
    # print (words)

    dictList2 = sorted(dictList2, key=len)
    foundFlag = False
    #Binary search for index of first word of length 'length'
    i = (len(dictList2)-1)//2
    m = len(dictList2)
    l = 0
    r = m-1
    while not (len(dictList2[i]) == length and len(dictList2[i-1]) < length):
        i = l + ((r-l)//2)
        if len(dictList2[i]) < length:
            l = i + 1
        elif len(dictList2[i]) >= length:
            r = i - 1 

    #Search words of length
    while len(dictList2[i]) == length:
        key = dictList2[i]
        i += 1

        #Validate word
        chars = [0]*26
        unique = False
        duplicate = False
        #Count number of each character
        for char in key:
            if char.isalpha():
                chars[alpha.index(char)] += 1

        for num in chars:
            if num == 1:
                unique = True
            if num > 1:
                duplicate = True
        
        #Test valid keys
        if unique == True and duplicate == True:
            count += 1
            plaintext = d_myszkowski(ciphertext,key)
            if utilities.is_plaintext(plaintext, dictList, 0.9):
                foundFlag = True
                break
        
    if foundFlag:
        print("key found after ", count, 'attempts')
        return plaintext,key
    return 'Failed', ''

def cryptanalysis3_myszkowski(ciphertext):    
    count = 0
    alpha = utilities.get_lower()
    dictList = utilities.load_dictionary("engmix.txt")

    # with open('engmix.txt', 'r', encoding=" ISO-8859-15") as f:
    #     dictList2 = f.read().split()

    # #Count words of length 5
    # words = []
    # validCount = 0
    # for word in dictList2:
    #     if len(word) == 5:
    #         #Validate word
    #         chars = [0]*26
    #         unique = False
    #         duplicate = False
    #         #Count number of each character
    #         for char in word:
    #             if char.isalpha():
    #                 chars[alpha.index(char)] += 1

    #         for num in chars:
    #             if num == 1:
    #                 unique = True
    #             if num > 1:
    #                 duplicate = True
    #         if unique and duplicate:
    #             words.append(word)
    # print (len(words))
    theKey = ''
    foundFlag = False
    for i in range(5):
        for j in range(5):
            if i != j:
                keys = ['ccccc', 'ccccc', 'ccccc']

                keys[0] = keys[0][:i] + 'a' + keys[0][i+1:]
                keys[0] = keys[0][:j] + 'b' + keys[0][j+1:]
                
                keys[1] = keys[1][:i] + 'a' + keys[1][i+1:]
                keys[1] = keys[1][:j] + 'd' + keys[1][j+1:]
                
                keys[2] = keys[2][:i] + 'd' + keys[2][i+1:]
                keys[2] = keys[2][:j] + 'e' + keys[2][j+1:]
                
                for key in keys:
                    count += 1
                    plaintext = d_myszkowski(ciphertext,key)
                    if utilities.is_plaintext(plaintext, dictList, 0.9):
                        theyKey = key
                        foundFlag = True
                        break
            if foundFlag:
                break
        if foundFlag:
            break
    if foundFlag:
        print("key found after ", count, 'attempts')
        return plaintext,key
    return 'Failed', ''

    plaintext = ''
    key = ''
    return plaintext,key


#---------------------------------
#           Q3: SDES Modes       #
#---------------------------------
# generic functions - specific functions in SDES.py
def e_SDES(plaintext,key,mode):
    if mode != 'ECB' and mode != 'CBC' and mode != 'OFB':
        print("Error(e_SDES): undefined mode", end='')
        return ''
    if plaintext == '':
        print("Error(e_SDES): Invalid input", end='')
        return ''
    # print(SDES.get_SDES_value('key_size'))
    # print(SDES.get_SDES_value('block_size'))
    if SDES.get_SDES_value('key_size') == '' or len(key) != int(SDES.get_SDES_value('key_size')):
            print("Error(e_SDES): Invalid key", end = '')
            return ''
    ciphertext = ''
    if mode == 'ECB':
        ciphertext = SDES.e_SDES_ECB(plaintext,key)
    return ciphertext

def d_SDES(ciphertext,key,mode):
    if mode != 'ECB' and mode != 'CBC' and mode != 'OFB':
        print("Error(d_SDES): undefined mode", end='')
        return ''
    if ciphertext == '':
        print("Error(d_SDES): Invalid input", end='')
        return ''
    if SDES.get_SDES_value('key_size') == '' or len(key) != int(SDES.get_SDES_value('key_size')):
            print("Error(d_SDES): Invalid key", end = '')
            return ''
    plaintext = ''
    if mode == 'ECB':
        plaintext = SDES.d_SDES_ECB(ciphertext,key)

    return plaintext

#---------------------------------
#           Q4: Double X       #
#---------------------------------
# Specific functions are in q4.py
def q4A(ciphertext):
    alpha = utilities.get_lower()
    foundFlag = False
    dictList = utilities.load_dictionary("engmix.txt")
    plaintext = q4.d_polybius(ciphertext)
    key1 = q4.get_polybius_square()

    for i in alpha:
        for j in alpha:
            plaintext2 = q4.d_columnarTrans(plaintext,i+j)
            if utilities.is_plaintext(plaintext2, dictList, 0.9):
                foundFlag = True
                key2 = i+j
                break
        if foundFlag:
            break
    if foundFlag:
        print('Ciphertext is all numbers therefore the first decryption is polybius.  Atbash and shift cipher decryption both failed.  Columnar transposition decryption succeeded.') #<----- edit this
        with open("q4A_plaintext.txt", 'w') as f:
            f.write(plaintext2)
        return plaintext2,(key1,key2)
    return "FAIL", (', ')

def q4B(ciphertext):
    alpha = utilities.get_lower()
    foundFlag = False
    dictList = utilities.load_dictionary("engmix.txt")

    # #Atbash decryption first
    # abtext = q4.d_atbash(ciphertext)
    # key1 = ''

    # #Try shift and columnar decryptions after atbash decryption
    # for i in range(1, 26):
    #     shifttext = q4.d_shift(abtext,(i, 'r'))
    #     if utilities.is_plaintext(shifttext, dictList, 0.9):
    #         foundFlag = True
    #         key2 = i
    #         break
    # if foundFlag:
    #     print('No numbers, we can assume neither encryption is polybius.  Case is preserved so encryptions are not Hill cipher') #<----- edit this
    #     return shifttext,(key1,key2)

    # for i in alpha:
    #     for j in alpha:
    #         coltext = q4.d_columnarTrans(abtext,i+j)
    #         if utilities.is_plaintext(coltext, dictList, 0.9):
    #             foundFlag = True
    #             key2 = i+j
    #             break
    #     if foundFlag:
    #         break
    # if foundFlag:
    #     print('No numbers, we can assume neither encryption is polybius.  Case is preserved so encryptions are not Hill cipher') #<----- edit this
    #     return coltext,(key1,key2)

    #Shift first
    for i in range(1, 26):
        shifttext = q4.d_shift(ciphertext,(i, 'r'))
        key1 = i
        
        #Check with atbash
        abtext = q4.d_atbash(shifttext)
        key2 = ''
        if utilities.is_plaintext(abtext, dictList, 0.9):
                foundFlag = True
        if foundFlag:
            print('No numbers, we can assume neither encryption is polybius.  Case is preserved so encryptions are not Hill cipher.  Atbash first decryption failed.') #<----- edit this
            return abtext,(key1,key2)

        #Check with columnar
        for i in alpha:
            for j in alpha:
                coltext = q4.d_columnarTrans(shifttext,i+j)
                if utilities.is_plaintext(coltext, dictList, 0.9):
                    foundFlag = True
                    key2 = i+j
                    break
            if foundFlag:
                break
        if foundFlag:
            print('No numbers, we can assume neither encryption is polybius.  Case is preserved so encryptions are not Hill cipher.  Atbash first decryption failed.  Shift first decryption succeeded with columnar as second decryption') #<----- edit this
            with open("q4B_plaintext.txt", 'w') as f:
                f.write(coltext)
            return coltext,(key1,key2)

    if foundFlag:
        print('No numbers, we can assume neither encryption is polybius.  Case is preserved so encryptions are not Hill cipher') #<----- edit this
        return shifttext,(key1,key2)


    print('No numbers, we can assume neither encryption is polybius.  Case is preserved so encryptions are not Hill cipher') #<----- edit this
    return "FAIL",(key1,key2)

def q4C(ciphertext):
    alpha = utilities.get_lower()
    foundFlag = False
    dictList = utilities.load_dictionary("engmix.txt")
    keys = 'abcde'

    #Hill cipher as first decryption
    for i in keys:
        for j in keys:
            for k in keys:
                for l in keys:

                    key = i+j+k+l
                    if not q4.has_det_inv(key):
                        continue

                    hillText = q4.d_hill(ciphertext, key)
                    key1 = key

                    #Atbash decryption second
                    abtext = q4.d_atbash(hillText)
                    if utilities.is_plaintext(abtext, dictList, 0.9):
                        foundFlag = True
                        key2 = ''
                    if foundFlag:
                        print('All uppper case but no numbers, signifying that a hill cipher was used.') #<----- edit this
                        return abtext,(key1,key2)
                            
                    #Shift decryption second
                    for a in range(0, 26):
                        shifttext = q4.d_shift(hillText,(a, 'r'))
                        if utilities.is_plaintext(shifttext, dictList, 0.9):
                            foundFlag = True
                            key2 = a
                            break
                    if foundFlag:
                        print('All uppper case but no numbers, signifying that a hill cipher was used.  I can also tell that columnar was not used as the punctuation all appears to be correct (no punctuation in the middle of words, quotes start and end, etc.).  Combination was found to be hill then shift after trial and error of hill, and shift/atbash') #<----- edit this
                        with open("q4C_plaintext.txt", 'w') as f:
                            f.write(shifttext)
                        return shifttext,(key1,key2)

    #Shift decryption first
    for a in range(0, 26):
        shifttext = q4.d_shift(ciphertext,(a, 'r'))
        key1 = a

        #Hill cipher second decryption
        for i in keys:
            for j in keys:
                for k in keys:
                    for l in keys:
                        key = i+j+k+l
                        if not q4.has_det_inv(key):
                            continue

                        hillText = q4.d_hill(shifttext, key)
                        
                        if utilities.is_plaintext(hillText, dictList, 0.9):
                            key2 = key
                            print('All uppper case but no numbers, signifying that a hill cipher was used.') #<----- edit this
                            return hillText,(key1,key2)

    #atbash first
    abtext = q4.d_atbash(ciphertext)
    key1 = ''

    #Hill cipher second decryption
    for i in keys:
        for j in keys:
            for k in keys:
                for l in keys:
                    key = i+j+k+l
                    if not q4.has_det_inv(key):
                        continue

                    hillText = q4.d_hill(abtext, key)
                    
                    if utilities.is_plaintext(hillText, dictList, 0.9):
                        key2 = key
                        print('All uppper case but no numbers, signifying that a hill cipher was used.') #<----- edit this
                        return hillText,(key1,key2)

    return "FAIL",(key1, key2)

#---------------------------------
# Q5: Public Key Cryptography    #
#---------------------------------
def get_RSAKey():
    with open('public_keys.txt', 'r') as f:
        text = f.read()
    for line in text.split("\n"):
        pubKey = line.split(" ")
        if pubKey[0] == "Joseph_Myc":
            break
    p = 30472889
    q = 27378359
    names = pubKey[0].split("_")
    name = names[0] + " " + names[1]
    m = int(pubKey[1])
    e = int(pubKey[2])
    n = int((p-1)*(q-1))
    #print(mod.mul_inv(7, 40))
    d = mod.mul_inv2(int(e), n)

    return [name,p,q,m,n,e,d]

def LRM(b,e,m):
    binary = (bin(e)[2:])
    vals = [1]
    #Get exponents
    for i in range(1, len(binary)):
        if binary[i] == '1':
            vals.append(vals[-1]*2)
            vals.append(vals[-1]+1)
        elif binary[i] == '0':
            vals.append(vals[-1]*2)
        else:
            print("ERROR: in exponent calculation")

    totals = []
    totals.append(b % m)

    for i in range(1, len(vals)):
        if (vals[i] - vals[i-1]) == 1:
            totals.append((totals[i-1] * totals[0]) % m)
        else:
            totals.append((totals[i-1] ** 2) % m)

    x = totals[-1]
    return x

def encode_mod96(text):
    baseString = utilities.get_RSA_baseString()
    num = 0
    length = 0
    for char in text[::-1]:
        i = baseString.index(char)
        num += i*(96**length)
        length += 1

    return num

def decode_mod96(num,block_size):
    baseString = utilities.get_RSA_baseString()
    text = ''
    length = block_size
    for i in range(block_size):
        if num > 0:
            val = num % 96
            num = num//96
            text = baseString[val] + text
    
    while len(text) < block_size:
        text = 'a' + text

    return text

def e_RSA(plaintext,key):
    ciphertext = ''

    while len(plaintext) % 6 != 0:
        plaintext += 'q'

    for i in range(0, len(plaintext), 6):
        chars = plaintext[i:i+6]
        charsNum = encode_mod96(chars)
        cipherNum = LRM(charsNum,key[1],key[0])
        cipherChars = decode_mod96(cipherNum, 8)
        ciphertext += cipherChars
    return ciphertext

def d_RSA(ciphertext,key):
    plaintext = ''

    for i in range(0, len(ciphertext), 8):
        chars = ciphertext[i:i+8]
        charsNum = encode_mod96(chars)
        plainNum = LRM(charsNum,key[1],key[0])
        plainChars = decode_mod96(plainNum, 6)
        plaintext += plainChars
    
    while plaintext[-1] == 'q':
        plaintext = plaintext[:-1]

    return plaintext
    
def verify_RSA(message):
    dictList = utilities.load_dictionary("engmix.txt")
    with open('public_keys.txt', 'r') as f:
        text = f.read()
    for line in text.split("\n"):
        pubKey = line.split(" ")
        names = pubKey[0].split("_")
        name = names[0] + " " + names[1]
        text = d_RSA(message,(int(pubKey[1]), int(pubKey[2])))         
        if utilities.is_plaintext(text, dictList, 0.9):
            return name, text
            
    return 'Unknown',''

# ----------------------------
#           Good Luck
# ----------------------------
