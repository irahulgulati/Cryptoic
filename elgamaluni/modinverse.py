import  math

def modInverse(b,m): 
    g = math.gcd(b, m)  
    if (g != 1): 
        return -1
    else:   
        return pow(b, m - 2, m) 
  
   
def modDivide(a,b,m): 
    a = a % m 
    inv = modInverse(b,m) 
    if(inv == -1): 
        return -1
    else: 
        return (inv*a) % m