import random
from .modinverse import modInverse, modDivide

def compute(pr,m,s,t):
    p=65537
    g=3
    r1=random.randint(1,100)
    r2=random.randint(1,100)
    y   =   pow(g,pr)%p
    X   =   pow(g,r1)%p
    Y   =  (m*pow(y,r1))%p
    W   =   pow(g,r2,p)
    Z   =   pow(y,r2,p)
    rdash   =  (r1+r2*s)
    sdash   =  (r2*t)
    Xdash   =  pow(g,rdash)%p
    Ydash   =  (pow(y,rdash)*m)%p 
    Wdash   =   pow(g,sdash,p)
    Zdash   =   pow(y,sdash,p)
    checkfordecryption   =   int(Z/(pow(W,pr) % p))
    if checkfordecryption == 1:
        xpower    =  pow(X,pr)
        decryptedMessage=modDivide(Y,xpower,p)
    else:
        decryptedMessage    =   "Decryption failed"
        print(decryptedMessage)
    result={
        'A':    y,
        'X':    X,
        'Y':    Y,  
        'W':    W,
        'Z':    Z,
        'rdash':    rdash,
        'sdash':    sdash,
        'Xdash':    Xdash,
        'Ydash':    Ydash,
        'Wdash':    Wdash,
        'Zdash':    Zdash,
        'decrypted': decryptedMessage
            }
    return result
