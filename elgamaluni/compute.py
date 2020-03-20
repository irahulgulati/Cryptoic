import random
def compute(pr,m,r,s):
    p=65537
    g=3
    r1=random.randint(1,100)
    r2=random.randint(1,100)
    A   =   pow(g,pr,p)
    X   =   (pow(A,r) * m) % p
    Y   =   (pow(g,r)) % p
    W   =   pow(A,s) % p
    Z   =   pow(g,s) % p
    rdash   =   r + s*r1
    sdash   =   s*r2
    Xdash   =   (pow(A,rdash)*m) % p
    Ydash   =   pow(g,rdash) % p
    Wdash   =   pow(A,sdash) % p
    Zdash   =   pow(g,sdash) % p
    checkfordecryption   =   int(W/(pow(Z,pr) % p))
    if checkfordecryption == 1:
        decryptedMessage    =   X/pow(Y,pr)
        print(decryptedMessage)
    else:
        decryptedMessage    =   "Decryption failed"

    result={
        'A':    A,
        'X':    X,
        'Y':    Y,  
        'W':    W,
        'Z':    Z,
        'rdash':    rdash,
        'sdash':    sdash,
        'Xdash':    Xdash,
        'Ydash':    Ydash,
        'Wdash':    Wdash,
        'Zdash':    Zdash
            }
    return result
