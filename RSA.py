import random

# GCD from Lecture 4 Slide 13
def euclidGCD(x, y):
    if y == 0:
        return x
    else:
        return euclidGCD(y, x%y)
    
# Prime Check
def primeCheck(x):
    if x < 2:
        return False
    else:
        for i in range(2,int(x/2)):
            if(x%i) == 0:
                return False
        return True

# Generating number
def generatePrimeNum():
    number = random.randint(10**6,10**7) # Range between 10^6 and 10^7
    while primeCheck(number) == False:
        number = random.randint(10**6,10**7)
    return number     

# Inverse
def mod_inverse(a, m):
    m0, x0, x1 = m, 0, 1
    while a > 1:
        q = a // m
        m, a = a % m, m
        x0, x1 = x1 - q * x0, x0
    return x1 + m0 if x1 < 0 else x1

# Generating keys
def keyGenerator():

    p = generatePrimeNum()
    q = generatePrimeNum()

    # Calculating system modulus and totient
    n = p * q
    totientFunc = (p-1)*(q-1)

    # Public key: (e, n)
    # Private key: (d, n)
    
    # Generating 'e'
    e = random.randint(2,totientFunc-1) # 1 < e < totientFunc
    while(euclidGCD(e,totientFunc)!=1):
        e = random.randint(2,totientFunc)

    # Generating 'd'
    d = mod_inverse(e, totientFunc)

    return ((e, n), (d, n))

# Encryption
def encrypt(publicKey, message):
    e, n = publicKey
    cipher = [pow(ord(char), e, n) for char in message]
    return cipher

# Decryption
def decrypt(privateKey, ciphertext):
    d, n = privateKey
    message = [chr(pow(char, d, n)) for char in ciphertext]
    return ''.join(message)