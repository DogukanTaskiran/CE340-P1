import random


# G.2 S-DES KEY GENERATION

# P10(k1, k2, k3, k4, k5, k6, k7, k8, k9, k10) = (k3, k5, k2, k7, k4, k10, k1, k9, k8, k6) 
def permute10(key):
    p10_order = [2, 4, 1, 6, 3, 9, 0, 8, 7, 5] 
    p10_key = [key[i] for i in p10_order]
    return p10_key

# Divided into 2 parts 5bit-5bit
def split_key(p10_key):
    leftHalf = p10_key[:5]
    rightHalf = p10_key[5:]
    return leftHalf, rightHalf

def one_bit_left_shift(half):
    shifted_half = half[1:] + [half[0]]
    return shifted_half

# P8(6,3,7,4,8,5,10,9)
def permute8(shiftedLeft, shiftedRight):
    combined_key = shiftedLeft + shiftedRight
    p8_order = [5, 2, 6, 3, 7, 4, 9, 8]
    subkey = [combined_key[i] for i in p8_order]
    # Key1
    return subkey

def generateSubkeys(key):
    p10_key = permute10(key)
    leftHalf, rightHalf = split_key(p10_key)

    shiftedLeft = one_bit_left_shift(leftHalf)
    shiftedRight = one_bit_left_shift(rightHalf)

    k1 = permute8(shiftedLeft, shiftedRight)
 
    shiftedLeft = one_bit_left_shift(leftHalf)
    shiftedRight = one_bit_left_shift(rightHalf)

    shiftedLeft = one_bit_left_shift(shiftedLeft)
    shiftedRight = one_bit_left_shift(shiftedRight)

    k2 = permute8(shiftedLeft, shiftedRight)

    return k1, k2

# G.3 S-DES ENCRYPTION

# IP 2 6 3 1 4 8 5 7
def initialPermutation(message):
    ipOrder = [1, 5, 2, 0, 3, 7, 4, 6]
    permutedText = [message[i - 1] for i in ipOrder]
    return permutedText

# IP^(–1) 4 1 3 5 7 2 8 6
def inversePermutation(ciphertext):
    ipInverseOrder = [3, 0, 2, 4, 6, 1, 7, 5]
    inversePermutedText = [ciphertext[i - 1] for i in ipInverseOrder]
    return inversePermutedText