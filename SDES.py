import random

# G.2 S-DES KEY GENERATION

# Expansion Permutation (4, 1, 2, 3, 2, 3, 4, 1)
expansionPermutation = [3, 0, 1, 2, 1, 2, 3, 0]

# P4 Permutation (2,4,3,1)
p4_permutation = [1, 3, 2, 0]

# P10 Permutation (k1, k2, k3, k4, k5, k6, k7, k8, k9, k10) = (k3, k5, k2, k7, k4, k10, k1, k9, k8, k6) 
p10_order = [2, 4, 1, 6, 3, 9, 0, 8, 7, 5] 

# P8 Permutation (6,3,7,4,8,5,10,9)
p8_order = [5, 2, 6, 3, 7, 4, 9, 8]

# IP 2 6 3 1 4 8 5 7
ipOrder = [1, 5, 2, 0, 3, 7, 4, 6]

# IP^(–1) 4 1 3 5 7 2 8 6
ipInverseOrder = [3, 0, 2, 4, 6, 1, 7, 5]


def permute10(key):
    p10_key = [key[i] for i in p10_order]
    return p10_key

# Divided into 2 parts 5bit-5bit
def split_key(p10_key):
    leftHalf = p10_key[:5]
    rightHalf = p10_key[5:]
    return leftHalf, rightHalf

def oneBitLeftShift(half):
    shiftedHalf = half[1:] + [half[0]]
    return shiftedHalf

def permute8(shiftedLeft, shiftedRight):
    combined_key = shiftedLeft + shiftedRight
    subkey = [combined_key[i-1] for i in p8_order]
    return subkey # Key 1

# Random key of 10 bits
def keyGenerator():
    key = ""
    for i in range(10):
        key += str(random.randint(0, 1))
    return key

def generateSubkeys(key):
    p10_key = permute10(key)
    leftHalf, rightHalf = split_key(p10_key)

    shiftedLeft = oneBitLeftShift(leftHalf)
    shiftedRight = oneBitLeftShift(rightHalf)

    k1 = permute8(shiftedLeft, shiftedRight)
 
    shiftedLeft = oneBitLeftShift(leftHalf)
    shiftedRight = oneBitLeftShift(rightHalf)

    shiftedLeft2 = oneBitLeftShift(shiftedLeft)
    shiftedRight2 = oneBitLeftShift(shiftedRight)

    k2 = permute8(shiftedLeft2, shiftedRight2)

    return k1, k2

# G.3 S-DES ENCRYPTION

def initialPermutation(message):
    permutedText = [message[i - 1] for i in ipOrder]
    return permutedText

def inversePermutation(ciphertext):
    inversePermutedText = [ciphertext[i - 1] for i in ipInverseOrder]
    return inversePermutedText

# fk(L,R) = (L xor F(R,SK),R)

def splitMessage(message):
    halfLenght = len(message) // 2
    leftHalf = message[:halfLenght]
    rightHalf = message[halfLenght:]
    return leftHalf, rightHalf

def encrypt(message, key):

    # Generating k1 and k2
    k1, k2 = generateSubkeys(key)    
    
    # Initial permutation
    ipMessage = initialPermutation(message)
    leftHalf, rightHalf = splitMessage(ipMessage)


    f_result, new_right = feistelFunction(ipMessage, k1) #burda sağı sokuyodu tüm ipyi soktum zaten kendi içinde bölüyo.
    new_left = [int(rightHalf[i]) ^ f_result[i] for i in range(4)]

    f_result, new_right = feistelFunction(new_right + new_left, k2)
    new_left = [int(new_right[i]) ^ f_result[i] for i in range(4)]

    encrypted_text = inversePermutation(new_right + new_left)
    return encrypted_text

def decrypt(ciphertext, key):

    # Generating k1 and k2
    k1, k2 = generateSubkeys(key)

    # Initial permutation
    ip = initialPermutation(ciphertext)

    # Split half
    leftHalf, rightHalf = splitMessage(ip)

    # Round 1
    fResult, newRight = feistelFunction(ip, k2)#burda sağı sokuyodu tüm ipyi soktum zaten kendi içinde bölüyo.
    newLeft = [int(leftHalf[i]) ^ fResult[i] for i in range(4)]

    # Round 2
    fResult, newRight = feistelFunction(newRight + newLeft, k1)
    newLeft = [int(rightHalf[i]) ^ fResult[i] for i in range(4)]

    # Final Permutation
    decryptedText = inversePermutation(newLeft + newRight)
    decryptedBinaryString = ''.join(map(str, decryptedText)) #convert list to string
    return decryptedBinaryString


# S-Box Definitions
sbox0 = [
    [1, 0, 3, 2],
    [3, 2, 1, 0],
    [0, 2, 1, 3],
    [3, 1, 3, 2]
]

sbox1 = [
    [0, 1, 2, 3],
    [2, 0, 1, 3],
    [3, 0, 1, 0],
    [2, 1, 0, 3]
]

# Switch Function
def switchFunction(bits):
    return bits[4:] + bits[:4]

def expansion(text):
    return ''.join(str(text[i-1]) for i in expansionPermutation)


# List based xor
def xor(left, right):
    left_int = [int(bit) for bit in left]
    right_int = [int(bit) for bit in right]
    return [left_int[i] ^ right_int[i] for i in range(len(left_int))]

# Integer sbox substitution
def sboxSubstitution(text, sbox):
    row = int(''.join(map(str, [text[0], text[3]])), 2)
    col = int(''.join(map(str, [text[1], text[2]])), 2)
    return [int(x) for x in format(sbox[row][col], '02b')]

# P4 Permutation
def p4Permute(text):
    permutedText = [text[i] for i in p4_permutation]
    return permutedText

def feistelFunction(ip, subkey):

    leftIp = ip[:4]
    rightIp = ip[4:]

    expandedRight = expansion(rightIp)
    xorResult = xor(expandedRight, subkey)
    sbox0Result = sboxSubstitution(xorResult[:4], sbox0)
    sbox1Result = sboxSubstitution(xorResult[4:], sbox1)
    sboxResult = sbox0Result + sbox1Result
    permutedResult = p4Permute(sboxResult)
    
    # fK(L, R) = (L xor F(R, SK), R)

    F = (xor(leftIp,permutedResult))

    return F,rightIp


# Converting string to binary
def stringToBinary(input_string):
    return ''.join(format(ord(char), '08b') for char in input_string)

# Converting binary to string
def binaryToString(input_binary):
    return ''.join(chr(int(input_binary[i:i+8], 2)) for i in range(0, len(input_binary), 8))

