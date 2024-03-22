import random

def euclidGCD(x,y): # from Lecture 4 Slide 13 
    if y == 0:
        return x
    else:   
        return euclidGCD(y, x%y)
    
def isPrime(x):
  if x<=1:
     return False
  else:
    for i in range(2,int(x/2)):
        if (x%i) == 0:
            return False
    return True

def primeGenerator(): # Range will be ---> 10^6 < number < 10^7
    number = random.randint(10,100)
    while isPrime(number)==False:
            number = random.randint(10,100)
    return number    

def encoder(message):
    return int.from_bytes(message.encode(), byteorder='big')

def decoder(encodedMessage):
    return encodedMessage.to_bytes((encodedMessage.bit_length()+7) // 8, byteorder='big').decode()

def keyGenerator(p,q):
    # Calculating system modulus and totient function Φ(n)
    n = p * q
    totientFunc = (p-1)*(q-1)

    # Generating 'e'
    e = random.randint(2,totientFunc-1) # 1 < e < totientFunc Φ(n)
    while (euclidGCD(e,totientFunc)!=1):
        e = random.randint(2,totientFunc-1)

    # Generating 'd'
    # Multiplicative Inverse of 'e'
    d = random.randint(0, n)  # 0 <= d <= n
    while (e * d) % totientFunc != 1:
        d = random.randint(0, n)
        if d > totientFunc:
            d = d - totientFunc
            break

    return n, e, d