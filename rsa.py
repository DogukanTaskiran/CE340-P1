import helpingFunctions
import random

def rsa_encryption(message):

    # https://rsa-calculator.netlify.app/

    # Generating 2 random prime numbers which are p and q
    q = helpingFunctions.primeGenerator()
    p = helpingFunctions.primeGenerator()
    
    if p == q:
        raise ValueError('q and p are same')
    elif helpingFunctions.isPrime(q) == False or helpingFunctions.isPrime(p) == False:
        raise ValueError('q and p must be prime')
    
    n, e, d = helpingFunctions.keyGenerator(p, q)

    encodedMessage = helpingFunctions.encoder(message)
    encryptedMessage = pow(encodedMessage, e, n) # (encodedMessage ^ e) % n

    # Keys
    public_key = (e,n)
    private_key = (d,n)

    print("Public Key  (e,n)  -> ", public_key)
    print("Private Key (d,n) -> ", private_key)
    print("Message           -> ", message)
    print("Encrypted Message -> ", encryptedMessage)
    print("*********************")

    return encryptedMessage, d, n

def rsa_decryption(encryptedMessage, d, n):

    decryptedMessage = pow(int(encryptedMessage), d, n) # (encryptedMessage ^ d) % n
    message = helpingFunctions.decoder(decryptedMessage)

    print("*********************")
    print("Decrypted Message -> ", decryptedMessage)
    print("Message           -> ", message)

    return decryptedMessage