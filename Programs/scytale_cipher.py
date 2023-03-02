'''
CP460 
Creation Date: 18/09/2019
Last Edit Date:18/09/2019
'''
import cryptoUtil
import math

'''
Parameters:
    Plaintext (String): the message to be encrypted
    Key (String): the diameter (# of rows)
Return:
    Ciphertext(String): the encrypted message
Description:
    Encrypt the given message using the scytale cipher.  Assume an infinite length rod(no limit on #columns)
'''
def e_scytale(plaintext, key):
    #Number of rows is the key, by definition
    r = int(key)
    #number of columns is the length of plaintext/key
    c = math.ceil(len(plaintext)/key)

    #Create an empty matrix for ciphertext (r*c)
    cipherMatrix = cryptoUtil.new_matrix(r, c, '')
    
    #Fill matrix horizontally with characters, pad empty slots with -1
    counter = 0
    for i in range(r):
        for i2 in range(c):
            if (counter < len(plaintext)):
                cipherMatrix[i][i2] = plaintext[counter]
            else:
                cipherMatrix[i][i2] = -1
            counter += 1

    ciphertext = ""

    #Convert matrix into a string (vertically)
    for i in range(c):
        for i2 in range(r):
            if (cipherMatrix[i2][i] != -1):
                ciphertext += cipherMatrix[i2][i]

    
    return ciphertext

'''
Parameters:
    Ciphertext(String): the encrypted message
    Key (String): the key to use for the encryption
Return:
    Plaintext (String): the message to be decrypted
Description
    Encrypt the given message using the Atbash cipher.  There is no key.
'''
def d_scytale(ciphertext, key):
    
    plaintext = e_atbash(ciphertext, None)
    return plaintext


'''
Parameters: None
Return: None
Description
    Test the Atbash cipher.
'''
def test_scytale ():
    
    print("Testing Scytale Cipher")
    print()

    plaintext = "GOODMORNING"
    print(e_scytale(plaintext, 3))
    return


test_scytale()