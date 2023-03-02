#get_lower, get_wordCount(text), shift_string, load_dictionary, text_to_words, analyze_text, is_plaintext
from cryptoUtil import get_lowercase

def get_charCount (text):
    return [text.count(chr(97+i))+text.count(chr(65+i)) for i in range(26)]

def get_freqTable():
    
    freqTable = [0.08167,0.01492,0.02782, 0.04253, 0.12702,0.02228, 0.02015,
    0.06094, 0.06966, 0.00153, 0.00772, 0.04025, 0.02406, 0.06749,
    0.07507, 0.01929, 0.00095, 0.05987, 0.06327, 0.09056, 0.02758,
    0.00978, 0.0236, 0.0015, 0.01974, 0.00074]
    
    return freqTable

def e_shift(plaintext, key):
    #----------------------------------------------------------------------------
    # Parameters:   plaintext (String)
    #               key (shifts, direction) (int, str)
    # Return:       ciphertext (string)
    # Description:  Encryption using shift cipher [monoalphabetic substitution]
    #               The alphabet is shifted as many as "shifts" using given direction
    #               non alpha characters --> no substitution
    #               VALID DIRECTION = 'l' or 'r'
    #               Encryption preserves character case
    #----------------------------------------------------------------------------
    ciphertext = ''
    alphabet = get_lowercase()
    shifts, direction = key

    if (shifts < 0):
        shifts *= -1
        direction = 'l' if direction == 'r' else 'r'

    shifts = shifts%26
    if (direction == 'l'):
        shifts = shifts
    else:
        shifts = 26-shifts

    ciphertext = ''
    for char in plaintext:
        if (char.lower() in alphabet):

            plainIndx = alphabet.index(char.lower())
            cipherIndx = (plainIndx + shifts)%26
            cipherChar = alphabet[cipherIndx]

            if (char.isupper()):
                ciphertext = cipherChar.upper()
            else:
                ciphertext = cipherChar

        else:
            ciphertext += char

    return ciphertext


def d_shift(plaintext, key):
    #----------------------------------------------------------------------------
    # Parameters:   plaintext (String)
    #               key (shifts, direction) (int, str)
    # Return:       ciphertext (string)
    # Description:  Decryption using shift cipher [monoalphabetic substitution]
    #               The alphabet is shifted as many as "shifts" using given direction
    #               non alpha characters --> no substitution
    #               VALID DIRECTION = 'l' or 'r'
    #               Encryption preserves character case
    #----------------------------------------------------------------------------
    if (key[1] == 'r'):
        direction = 'l'
    else:
        direction = 'r'
    return e_shift(ciphertext, (key[0], direction))

def cryptanalysis_shift(ciphertext):
    #----------------------------------------------------------------------------
    # Parameters:   plaintext (String)
    #               key (shifts, direction) (int, str)
    # Return:       ciphertext (string)
    # Description:  Encryption using shift cipher [monoalphabetic substitution]
    #               The alphabet is shifted as many as "shifts" using given direction
    #               non alpha characters --> no substitution
    #               VALID DIRECTION = 'l' or 'r'
    #               Encryption preserves character case
    #----------------------------------------------------------------------------
    alphabet = get_lowercase()
    for i in range(26):
        plaintext = d_shift(ciphertext, (i, 'l'))
        if is_plaintext(plaintext, "engmix.txt", 0.8):
            print('Key found: ', (i, 'l'))
            print('plaintext: ', plaintext)
    
    print('Cryptoanalysis failed! no key found')
    return ''

def cryptanalysis2_shift(ciphertext):
    #----------------------------------------------------------------------------
    # Parameters:   plaintext (String)
    #               key (shifts, direction) (int, str)
    # Return:       ciphertext (string)
    # Description:  Encryption using shift cipher [monoalphabetic substitution]
    #               The alphabet is shifted as many as "shifts" using given direction
    #               non alpha characters --> no substitution
    #               VALID DIRECTION = 'l' or 'r'
    #               Encryption preserves character case
    #----------------------------------------------------------------------------
    charCount = get_charCount (ciphertext)
    alphabet = get_lowercase()

    maxChar = 0
    for i in range(l, len(charCount)):
        if charCount[i] > charCount[maxChar]:
            maxChar=i

    freqLetters = ['e', 't', 'a']
    for letter in freqLetters:
        key = alphabet.index(alphabet[maxChar]) - alphabet.index(letter)
        key = (key*1, 'r') if key < 0 else (key, 'l')
        plaintext = d_shift(ciphertext, key)
        if is_plaintext(plaintext, "engmix.txt", 0.8):
            print('Key found: ', key, '\nplaintext: ', plaintext)
            return key, plaintext
    print("Cryptanalysis failed! no key found")
    return '', ''

def get_chiSquared(text):
    #----------------------------------------------------------------------------
    # Parameters:   text(string)
    # Return:       double (result of chi-squared)
    # Description:  Calculates the Chi-squared statistics
    #               chi_squaraed = for i=0(a) to i=25(z):
    #                               sum(Ci-Ei)^2 / Ei
    #----------------------------------------------------------------------------
    freqTable = get_freqTable()
    charCount = get_charCount(text)

    result = 0
    for i in range(26):
        Ci = charCount[i]
        Ei = freqTable[i]*len(text)


def cryptanalysis3_shift(ciphertext):
    #----------------------------------------------------------------------------
    # Parameters:   plaintext (String)
    #               key (shifts, direction) (int, str)
    # Return:       ciphertext (string)
    # Description:  Encryption using shift cipher [monoalphabetic substitution]
    #               The alphabet is shifted as many as "shifts" using given direction
    #               non alpha characters --> no substitution
    #               VALID DIRECTION = 'l' or 'r'
    #               Encryption preserves character case
    #----------------------------------------------------------------------------
    chiList = [get_chiSquared(d_shift(ciphertext, (i, 'l'))) for i in range(26)]
    key = chiList.index(min(chiList))
    plaintext = d_shift(ciphertext, key)
    return key, plaintext

def e_ROT13(plaintext, key):
    return e_shift(plaintext, (13, 'l'))

def d_ROT13(ciphertext, key):
    return e_ROT13(ciphertext, key)



