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

def primeGenerator(): # 10^6 < number < 10^7
    number = random.randint(10,100)
    while isPrime(number)==False:
            number = random.randint(10,100)
    return number    