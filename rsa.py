import helpingFunctions
import random

def keyGenerator():

    q = helpingFunctions.primeGenerator()
    p = helpingFunctions.primeGenerator()

    if p==q:
        raise ValueError('q and p are same')
    elif helpingFunctions.isPrime(q) == False or helpingFunctions.isPrime(p) == False:
        raise ValueError('q and p must be prime')

    n = p * q

    totientFunc = (p-1)*(q-1)

    # Part E
    e = random.randint(2,totientFunc-1) # 1 < e < totientFunc
    while (helpingFunctions.euclidGCD(e,totientFunc)!=1):
        e = random.randint(2,totientFunc-1)

    # Part D
    d = random.randint(0, n)  # 0 =< d =< n
    while (e * d) % totientFunc != 1:
        d = random.randint(0, n)
        if d > totientFunc:
            d = d - totientFunc
            break


    public_key = (e,n)
    private_key = (d,n)

    return public_key, private_key

def rsa_encrypt(message, public_key):
    e, n = public_key
    ciphertext = [pow(ord(element), e, n) for element in message]  # (M^e)%n
    return ciphertext

def rsa_decrypt(ciphertext, private_key):
    d, n = private_key
    message = [pow(ord(element), d, n) for element in ciphertext]   # (C^d)%n

    output = [chr(int(element)) for element in message]
    return ''.join(output)