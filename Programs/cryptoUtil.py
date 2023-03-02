'''
CP460 
Creation Date: 16/09/2019
Last Edit Date:16/09/2019
Cryptography Utilities
'''



def get_lowercase():
    '''
        Parameters: None
        Return: 
            alphabet (String): lower case alphabet
        Description: Return a string containing the lower case alphabet
    '''
    #alphabet = string.ascii_lowercase
    #return "".join([chr(ord('a')+i) for i in range(26)])

    alphabet = ""
    for i in range (26):
        tempChar = ord('a') + i
        char = chr(tempChar)
        alphabet += char

    return alphabet

def file_to_text(filename):
    '''
        Parameters:
            filename(String):
        Return: 
            contents(String): the text in the file
        Description: return a string of the contents
    '''
    #with
    inFile = open(filename, "r")
    contents = inFile.read()
    inFile.close()

    return contents

def text_to_file(text, filename):
    '''
        Parameters:
            filename(String):
            text(String): the text to write
        Return: 
            
        Description: return a string of the contents
    '''
    #with
    outFile = open(filename, 'w')
    outFile.write(text)
    outFile.close
    return

def new_matrix(r, c, pad):
    '''
        Parameters:
            r (int): # of rows
            c (int): # of columns
            pad (str, int, float)
        Return: 
            matrix (2d list)
        Description: Create an empty matrix of size r*c.  
                    All elements initialized to pad.  
                    Default row and column size is 2.
    '''
    
    if r>2:
        r = r
    else:
        r = 2

    if (c>2):
        c = c
    else:
        c = 2

    return [[pad]*c for i in range (r)]

def shift_string(s, n, d):
    '''
        Parameters:
            s (String): input string
            n (int): # of shifts
            d (str): direction 'r' or 'l'
        Return: 
            string (after shifts)
        Description: Shift given string n times in given direction
    '''
    if (d != 'r' and d != 'l'):
        print("Error (shift_string): invalid direction")
        return ''
    
    if (n<0):
        n = n*-1

        if (d=='r'):
            d = 'l' 
        else:
            d = 'r'
        
    if (s=='' or n==0):
        return s
    
    if (d=='l'):
        s = s[n:]+s[:n]
    else:
        s = s[-1*n:]+s[:-1*n]

    return s

def get_outWheel(pointer):
    outWheel = cryptoUtil.get_lower().upper()
    for i in range(10):
        outWheel += str(i)
    pointerIndex = outWheel.index(pointer)
    outWheel = cryptoUtil.shift_string(outWheel, pointerIndex, "1")
    return outWheel

def get_inWheel(pointer):
    inWheel = 'k0v9plj8m2r7d315g'


def e_alberti (plaintext, key):
    ciphertext = ''
    outWheel = get_outWheel(key[0])
    inWheel = get+inWheel(key[1])

    for char in plaintext:
        if char.upper() in outWheel:
            indx = outWheel.index(char.upper())
            ciphertext += inWheel[indx]
        else:
            ciphertext += char
        return ciphertext

def d_alberti (ciphertext, key):
    plaintext = ''
    outWheel = get_outWheel(key[0])
    inWheel = get+inWheel(key[1])

    for char in ciphertext:
        if char.lower() in inWheel:
            indx = inWheel.index(char.lower())
            plaintext = outWheel[indx]
        else:
            plaintext += char

    return plaintext

def cryptAnalysis_alberti(cipherText, outWheel, inWheel):
    plaintext = ''
    for i in range(len(outWheel)):#this outer loop is not needed
        for j in range (len(inWheel)):
            key = outWheel[0] + inWheel[0]
            plaintext = d_alberti(ciphertext, key)
            result = cryptoUtil.is_plaintext(plaintext, "engmix.txt", 0.8)
            if result:
                break
            else:
                print('Key', key, 'failed')
                inWheel = cryptoUtil.shift_string(inWheel, 1, '1')
        outWheel = cryptoUtil.shift_string(outWheel, 1,'1')#this is not needed
    return key, plaintext


def get_string_perm(s, permList):
#----------------------------------------------------------------------------
# Parameters:   s (String)
# Return:       permList (list)
# Description:  Generate all permutations of a given string. Each perm is 
#               stored as an item in a list
#----------------------------------------------------------------------------
    #method 1: built in function
    permList = list(itertools.permutations)

    return permList