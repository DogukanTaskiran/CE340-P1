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

# fk(L,R) = (L xor F(R,SK),R)

def split_message(message):
    half_len = len(message) // 2
    left_half = message[:half_len]
    right_half = message[half_len:]
    return left_half, right_half

def binary_to_string(binary_list):
    # Ikili listeyi 8 bitlik parçalara ayır
    chunks = [binary_list[i:i+8] for i in range(0, len(binary_list), 8)]
    # Her 8 bitlik parçayı ASCII karakterine dönüştür ve birleştir
    string = ''.join([chr(int(''.join(map(str, chunk)), 2)) for chunk in chunks])
    return string

def string_to_binary(string):
    binary_list = []
    for char in string:
        binary_char = bin(ord(char))[2:].zfill(8)
        binary_list.extend([int(bit) for bit in binary_char])
    return binary_list

def encrypt(message, key):
    k1, k2 = generateSubkeys(key)
    ip_message = initialPermutation(message)
    left_half, right_half = split_message(ip_message)

    # Round 1
    f_result = feistel_function(right_half, k1)
    new_right = xor(left_half, f_result)
    # Round 2
    f_result = feistel_function(new_right, k2)
    new_left = xor(right_half, f_result)

    # Final Permutation
    encrypted_text = inversePermutation(new_left + new_right)
    return encrypted_text

def decrypt(ciphertext, key):
    k1, k2 = generateSubkeys(key)
    ip_ciphertext = initialPermutation(ciphertext)
    left_half, right_half = split_message(ip_ciphertext)

        # Round 1
    f_result = feistel_function(right_half, k2)
    new_right = xor(left_half, f_result)
    # Round 2
    f_result = feistel_function(new_right, k1)
    new_left = xor(right_half, f_result)

    # Final Permutation
    decrypted_text = inversePermutation(new_left + new_right)
    return decrypted_text


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

# Expansion Permutation
expansion_permutation = [3, 0, 1, 2, 1, 2, 3, 0]

# P4 Permutation
p4_permutation = [1, 3, 2, 0]

def expansion(text):
    expanded_text = [text[i] for i in expansion_permutation]
    return expanded_text

def xor(left, right):
    return [left[i] ^ right[i] for i in range(len(left))]

def sbox_substitution(text, sbox):
    row = int(''.join(map(str, [text[0], text[3]])), 2)
    col = int(''.join(map(str, [text[1], text[2]])), 2)
    return [int(x) for x in format(sbox[row][col], '02b')]

def p4_permute(text):
    permuted_text = [text[i] for i in p4_permutation]
    return permuted_text

def feistel_function(right, subkey):
    expanded_right = expansion(right)
    xor_result = xor(expanded_right, subkey)
    sbox0_result = sbox_substitution(xor_result[:4], sbox0)
    sbox1_result = sbox_substitution(xor_result[4:], sbox1)
    sbox_result = sbox0_result + sbox1_result
    permuted_result = p4_permute(sbox_result)
    return permuted_result

def string_to_binary(string):
    binary_list = []
    for char in string:
        binary_char = bin(ord(char))[2:].zfill(8)
        binary_list.extend([int(bit) for bit in binary_char])
    return binary_list

def main():
    message = input("Enter the message: ")
    key = input("Enter the key (10-bit binary): ")

    # Convert string message to binary
    binary_message = string_to_binary(message)
    key_binary = [int(bit) for bit in key]

    print("Encrypting using key:", key)  # Anahtarı print et

    # Encrypt the message
    encrypted_message = encrypt(binary_message, key_binary)
    print("Encrypted Message:", binary_to_string(encrypted_message))

    # Decrypt the message
    decrypted_message = decrypt(encrypted_message, key_binary)
    print("Decrypted Message:", binary_to_string(decrypted_message))