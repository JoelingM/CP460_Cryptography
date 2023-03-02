'''
CP460 
Creation Date: 18/09/2019
Last Edit Date:18/09/2019
'''
import cryptoUtil
import math

def get_outWheel(pointer):
    outWheel = get_lowercase().upper()
    for i in range(10):
        outWheel += str(i)
    pointer_index = outWheel.index(pointer)
    outWheel = cryptoUtil.shift_string(outWheel, pointer_index, 'l')
    return outWheel

def get_inWheel(pointer):
                   #1?
    inWheel = 'k0v9plj8m2r7d3l5g4a6zteunwbosfchyqix'
    pointer_index = inWheel.index(pointer)
    inWheel = cryptoUtil.shift_string(inWheel, pointer_index, 'l')
    return inWheel 

'''
Parameters:
    Plaintext (String): the message to be encrypted
    Key (String): the diameter (# of rows)
Return:
    Ciphertext(String): the encrypted message
Description:
    Encrypt the given message using the scytale cipher.  Assume an infinite length rod(no limit on #columns)
'''
