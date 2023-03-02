#--------------------------
# Your Name and ID Joseph Myc | 160 740 900
# CP460 (Fall 2019)
# Assignment 1
#--------------------------


import math
import string

#---------------------------------
#       Given Functions          #
#---------------------------------
#-----------------------------------------------------------
# Parameters:   fileName (string)
# Return:       contents (string)
# Description:  Utility function to read contents of a file
#               Can be used to read plaintext or ciphertext
#-----------------------------------------------------------
def file_to_text(fileName):
    inFile = open(fileName,'r')
    contents = inFile.read()
    inFile.close()
    return contents

#-----------------------------------------------------------
# Parameters:   text (string)
#               filename (string)            
# Return:       none
# Description:  Utility function to write any given text to a file
#               If file already exist, previous content will be over-written
#-----------------------------------------------------------
def text_to_file(text, filename):
    outFile = open(filename,'w')
    outFile.write(text)
    outFile.close()
    return

#-----------------------------------------------------------
# Parameters:   r: #rows (int)
#               c: #columns (int)
#               pad (str,int,double)
# Return:       empty matrix (2D List)
# Description:  Create an empty matrix of size r x c
#               All elements initialized to pad
#               Default row and column size is 2
#-----------------------------------------------------------
def new_matrix(r,c,pad):
    r = r if r >= 2 else 2
    c = c if c>=2 else 2
    return [[pad] * c for i in range(r)]

#-----------------------------------------------------------
# Parameters:   marix (2D List)
# Return:       None
# Description:  prints a matrix each row in a separate line
#               Assumes given parameter is a valid matrix
#-----------------------------------------------------------
def print_matrix(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            print(matrix[i][j],end='\t')
        print()
    return
#-----------------------------------------------------------
# Parameters:   marix (2D List)
# Return:       text (string)
# Description:  convert a 2D list of characters to a string
#               left to right, then top to bottom
#               Assumes given matrix is a valid 2D character list
#-----------------------------------------------------------
def matrix_to_string(matrix):
    text = ""
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            text+=matrix[i][j]
    return text

#--------------------------------------------------------------
# Parameters:   plaintext(string)
#               key (string)
# Return:       ciphertext (string)
# Description:  Encryption using Scytale Cipher
#               Key is the diameter, i.e. # rows
#               Assume infinte length rod (infinte #columns)
#--------------------------------------------------------------
def e_scytale(plaintext, key):
    # By definition, number of rows is key
    r = int(key)
    # number of columns is the length of ciphertext/# rows    
    c = int(math.ceil(len(plaintext)/key))
    # create an empty matrix for ciphertext rxc
    cipherMatrix = new_matrix(r,c,"")

    # fill matrix horizontally with characters, pad empty slots with -1
    counter = 0
    for i in range(r):
        for j in range(c):
            cipherMatrix[i][j] = plaintext[counter] if counter < len(plaintext) else -1
            counter+=1

    #convert matrix into a string (vertically)
    ciphertext = ""
    for i in range(c):
        for j in range(r):
            if cipherMatrix[j][i]!=-1:
                ciphertext+=cipherMatrix[j][i]
    return ciphertext


#---------------------------------
#       Problem 1                #
#---------------------------------
      
#----------------------------------------------------
# Parameters:   ciphertext(string)
#               key (string)
# Return:       plaintext (string)
# Description:  Decryption using Scytale Cipher
#               Assumes key is a valid integer in string format             
#---------------------------------------------------
def d_scytale(ciphertext, key):
    plaintext = ''
    # By definition, number of columns is key
    r = int(key)
    #print("r:", r)
    # number of rows is the length of ciphertext/# rows    
    c = int(math.ceil(len(ciphertext)/key))
    #print("c:", c)

    #Number of leftover spaces
    rem = int(r*c - len(ciphertext))
    #print("calculation:", r*c, "-", len(ciphertext))
    #print("rem:", rem)

    if (c <= rem):
        return ""

    # create an empty matrix for plaintext rxc
    plainMatrix = new_matrix(c,r,"")

    # fill matrix horizontally with characters, pad empty slots with -1
    counter = 0
    for i in range(c):
        for j in range(r):
            #if the row needs to end with a blank space
            if (c-rem <= i and j == r-1):
                plainMatrix[i][j] = -1

            else:
                #print("Counter: ", counter)
                plainMatrix[i][j] = ciphertext[counter]                    
                counter+=1

            

    #print("decryption matrix:")
    #print_matrix(plainMatrix)

    #convert matrix into a string (vertically)
    ciphertext = ""
    for i in range(r):
        for j in range(c):
            if plainMatrix[j][i]!=-1:
                plaintext+=plainMatrix[j][i]
    
    # your code here
    return plaintext

#---------------------------------
#       Problem 2                #
#---------------------------------

#-----------------------------------------------------------
# Parameters:   dictFile (string): filename
# Return:       list of words (list)
# Description:  Reads a given dictionary file
#               dictionary file is assumed to be formatted: each word in a separate line
#               Returns a list of strings, each pertaining to a dictionary word
#-----------------------------------------------------------
def load_dictionary(dictFile):
    dictList = []
    # your code here
    with open(dictFile, 'r', encoding="mbcs") as file:
        for line in file:
            line = line.strip('\n')
            dictList.append(line)
        # textStr = file_to_text(file)
        # dictList = textStr.splitlines()
    return dictList

#-------------------------------------------------------------------
# Parameters:   text (string)
# Return:       list of words (list)
# Description:  Reads a given text
#               Each word is saved as an element in a list. 
#               Returns a list of strings, each pertaining to a word in file
#               Gets rid of all punctuation at the start and at the end 
#-------------------------------------------------------------------
def text_to_words(text):

    #Split text into the list
    wordList = []
    wordList = text.split()

    #Clean list
    count = 0
    for word in wordList:
        wordList[count] = word.strip(string.punctuation)
        count += 1

    return wordList

#-----------------------------------------------------------
# Parameters:   text (string)
#               dictFile (string): dictionary file
# Return:       (#matches, #mismatches)
# Description:  Reads a given text, checks if each word appears in dictionary
#               Returns a tuple of number of matches and number of mismatches.
#               Words are compared in lowercase.
#-----------------------------------------------------------
def analyze_text(text, dictFile):
    dictArray = load_dictionary(dictFile)
    textArray = text_to_words(text)
    matches = 0
    mismatches = 0

    for word in textArray:
        if (word.lower() in dictArray):
            matches += 1
        else:
            mismatches += 1

    return(matches,mismatches)

#-----------------------------------------------------------
# Parameters:   text (string)
#               dictFile (string): dictionary file
#               threshold (float): number between 0 to 1
# Return:       True/False
# Description:  Check if a given file is a plaintext
#               If #matches/#words >= threshold --> True
#                   otherwise --> False
#               If invalid threshold given, default is 0.9
#               An empty string is assumed to be non-plaintext.
#-----------------------------------------------------------
def is_plaintext(text, dictFile, threshold):

    if (text == ""):
        return False

    result = analyze_text(text, dictFile)    

    #invalid threshold
    if (threshold > 1 or threshold < 0):
        threshold = 0.9

    #threshold calculation
    if (result[0]/(result[0]+result[1]) > threshold):
        return True

    return False

#---------------------------------
#       Problem 3                #
#---------------------------------
      
#----------------------------------------------------
# Parameters:   cipherFile (string)
#               dictFile (string)
#               startKey (int)
#               endKey (int)
#               threshold (float)
# Return:       key (string)
# Description:  Apply brute-force to break scytale cipher
#               Valid key range: 2-100 (if invalid --> print error msg and return '')
#               Valid threshold: 0-1 (if invalid --> print error msg and return '')
#               If decryption is successful --> print plaintext and return key
#               If decrytpoin fails: print error msg and return ''
#---------------------------------------------------
def cryptanalysis_scytale(cipherFile, dictFile, startKey, endKey, threshold):
    #Invalid entry value check
    if (startKey < 2 or endKey > 100):
        print("Invalid key range. Operation aborted!")
        return ""
    if (threshold > 1 or threshold < 0):
        print("Invalid threshold value. Operation aborted!")
        return ""
    
    #Get text to decrypt
    ciphertext = file_to_text(cipherFile)
    
    for i in range(startKey, endKey+1):
        #Attempt decryption
        plaintext = d_scytale(ciphertext, i)

        #Check decryption
        if (is_plaintext(plaintext, dictFile, threshold)):
            print("Key found: ", i)
            print(plaintext)
            return str(i);
        else:
            print("key ", i, " failed")

    print("No key was found")
    return '' # you may change this

#---------------------------------
#       Problem 4                #
#---------------------------------
      
#----------------------------------------------------
# Parameters:   None
# Return:       polybius_square (string)
# Description:  Returns the following polybius square
#               as a sequential string:
#               [1] [2]  [3] [4] [5] [6] [7] [8]
#           [1]      !    "   #   $   %   &   '
#           [2]  (   )    *   +   '   -   .   /
#           [3]  0   1    2   3   4   5   6   7
#           [4]  8   9    :   ;   <   =   >   ?
#           [5]  @   A    B   C   D   E   F   G
#           [6]  H   I    J   K   L   M   N   O
#           [7]  P   Q    R   S   T   U   V   W
#           [8]  X   Y    Z   [   \   ]   ^   _
#---------------------------------------------------
def get_polybius_square():
    polybius_square = ''
    for i in range(32, 96):
        polybius_square += chr(i)
    # your code here
    return polybius_square

#--------------------------------------------------------------
# Parameters:   plaintext(string)
#               key (none)
# Return:       ciphertext (string)
# Description:  Encryption using Polybius Square
#--------------------------------------------------------------
def e_polybius(plaintext, key):
    ciphertext = ''
    poly = get_polybius_square()

    #Loop through text
    for pchar in plaintext:

        #Check for end of line char
        if (pchar == '\n'):
            ciphertext += pchar

        else:
            #Capitalize
            if (pchar.islower()):
                pchar = pchar.upper()

            #Add numbers to ciphertext
            charI = poly.find(pchar)
            #print(pchar, ", ", charI)
            if (charI != -1):
                ciphertext += str(math.floor(charI/8) + 1)
                ciphertext += str((charI%8) + 1)

    return ciphertext

#---------------------------------
#       Problem 5                #
#---------------------------------

#-------------------------------------------------------
# Parameters:   ciphertext(string)
#               key (none)
# Return:       plaintext (string)
# Description:  Decryption using Polybius Square Cipher
#               Detects invalid ciphertext --> print error msg and return ''
#               Case 1: #of chars (other than \n) is not even
#               Case 2: the ciphertext contains non-numerical chars (except \n')
#-------------------------------------------------------
def d_polybius(ciphertext, key):
    plaintext = ''
    poly = get_polybius_square()
    #Remove newline characters
    stripString = ciphertext.replace('\n', '')
    #Check that there is an even number of number
    if ( (len(stripString)) % 2 != 0):
        print("Invalid ciphertext! Decryption Failed!")
        return ''

    for char in stripString:
        if (not char.isdigit()):
            print("Invalid ciphertext! Decryption Failed!")
            return ''

    i = 0
    while (i < len(ciphertext)):
        
        #Handle newline character (fails if \n#\n).
        if (ciphertext[i] == '\n'):
            plaintext += ciphertext[i]
            i += 1
        #Decode each character
        else:
            plaintext += poly[(int(ciphertext[i])-1)*8 + (int(ciphertext[i+1])-1)]
            i+= 2

    return plaintext
