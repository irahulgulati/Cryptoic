import sympy
import math
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

def compute(v,p,q,e,m):
	message = {}
	if sympy.isprime(p):
		if sympy.isprime(q):
			n = p*q
			phiN=(p-1)*(q-1)
			# return phiN
			newgcd=gcd(phiN,e)
			if newgcd == 1:
				d 	= privatekey(e,phiN)
				if v==1:
					ctext = encrypt(m,e,n)
					ptext 	= decrypt(ctext,d,n)
					message = {
						'plain':ptext,
						'crypted':ctext,
						'privateKey':d,
						'phiN':phiN
					}
					return message
			else:
				message = {
						'msg':"Please choose e as 1<e<N",
					}
				return message
		else:
			message = {
				'msg': "Please enter Prime numbers"
			}
			return message
	else:
		message	=	{
			'msg':  "Please enter Prime numbers"
		}
		return message
	