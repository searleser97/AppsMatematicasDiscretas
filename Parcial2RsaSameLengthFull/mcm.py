from fractions import gcd

def mcm(a,b):
	result = int((a*b)/gcd(a,b))
	return result