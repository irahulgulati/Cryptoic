import sympy
def gcd(a,b): 
    if(b==0): 
        return a 
    else: 
        return gcd(b,a%b) 
def privatekey(x, y):
	def eea(a,b):
		if b == 0: return (1,0)
		(q,r) = (a//b,a%b)
		(s,t) = eea(b,r)
		return (t, s-(q*t))
	inv = eea(x,y)[0]
	if inv < 1 : inv += y
	return inv

def encrypt(message, pub_key,n):
	cypher_text= [(ord(char) ** pub_key) % n for char in message]
	return cypher_text
def decrypt(cypher_text:str,pri_key,n):
	plain_text = ''
	plain_text = [(char ** pri_key)%n for char in cypher_text]
	pt=[chr(plain) for plain in plain_text]
	plaintext=''.join(pt)
	return plaintext

def compute(x,m,r1,r2):
	p=65537
	g=3
	y		=	pow(g,x,p) #Calculating Public key
	c1		=	pow(g,r1,p)  #calculating c1
	c2		=	m*(pow(y,r1)%p)
	# c2new	=	c2 % p  #Calculating c2
	c1prime	=	(c1*pow(g,r2))%p
	c2prime	=	(c2*pow(y,r2,p))%p
	decrypt	=	pow(c1,x,p)
	finaldecrypt	=	int((c2/decrypt) % p)
	print(finaldecrypt)
	result = {
		'y':y,
		'c1':c1,
		'c2':c2,
		'c1p':c1prime,
		'c2p':c2prime,
		'decrypt':finaldecrypt
	}
	return result
