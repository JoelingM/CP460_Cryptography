'''
CP460 
Creation Date: 16/09/2019
Last Edit Date:16/09/2019
'''
import cryptoUtil

'''
Parameters:
    Plaintext (String): the message to be encrypted
    Key (String): the key to use for the encryption
Return:
    Ciphertext(String): the encrypted message
Description:
    Encrypt the given message using the Atbash cipher.  There is no key.
'''
def e_atbash(plaintext, key):
    
    ciphertext = ""
    alphabet = get_lowercase()

    for plainChar in plaintext:
        #Check if it is a letter
        if (plainChar.isalpha()):

            #Check if it is upper case
            upper = False
            if (plainChar.isupper()):
                upper = True 

            cipherChar = alphabet[25 - alphabet.index(plainChar.lower())]
            
            if (upper):
                ciphertext += cipherChar.upper()
            else:
                ciphertext += cipherChar

        else:
            ciphertext += plainChar

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
def d_atbash(ciphertext, key):
    
    plaintext = e_atbash(ciphertext, None)
    return plaintext


'''
Parameters: None
Return: None
Description
    Test the Atbash cipher.
'''
def test_atbash ():
    print("Testing Atbash Cipher")
    print()

    plaintextFile = input('Enter plaintext file name: ')
    plaintext = cryptoUtil.file_to_text(plaintextFile)
    print()

    print("Plaintext before encryption:")
    print(plaintext)
    print()

    ciphertext = e_atbash(plaintext, None)
    print("Ciphertext after encryption")
    print(ciphertext)
    print()

    plaintext = d_atbash(ciphertext, None)
    print("Plaintext after decryption")
    print(plaintext)
    print()

    return


test_atbash()