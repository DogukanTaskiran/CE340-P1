import helpingFunctions
import random

def rsa(p,q):

    n = p * q

    totientFunc = (p-1)*(q-1)

    e = random.randint(2,totientFunc-1) # 1 < e < totientFunc

    while (helpingFunctions.euclidGCD(e,totientFunc)!=1):
        e = random.randint(2,totientFunc-1)

    # Debugger to see variables
    #print(f"p: {p}, q: {q}, n: {n}, totientFunc: {totientFunc}, e: {e}")

    d = random.randint(0,n) # 0 < d < n

    c = e*d

    while (helpingFunctions.euclidGCD(e,d)!=1 and c!=1%n):
        d = random.randint(0,n)


    # Debugger to see variables
    print(f"p: {p}, q: {q}, n: {n}, totientFunc: {totientFunc}, e: {e}, d: {d}")