import helpingFunctions
import random
def rsa(p,q):

    n = p * q

    totientFunc = (p-1)*(q-1)

    # Part E
    e = random.randint(2,totientFunc-1) # 1 < e < totientFunc
    while (helpingFunctions.euclidGCD(e,totientFunc)!=1):
        e = random.randint(2,totientFunc-1)

    # Part D
    d = random.randint(0,n) # 0 < d < n

    while ((e*d) % totientFunc != 1):
        d = random.randint(0,n)
        if (d > totientFunc):
            d = d-totientFunc

    # Debugger to see variables **************************************************************
    print(f"p: {p}, q: {q}, n: {n}, totientFunc: {totientFunc}, e: {e}, d: {d}")