class Polynomial(dict):
	def __init__(self,n):
		if isinstance(n,Polynomial):
			dict.__init__(self,n)
		elif type(n) == type({}):
			dict.__init__(self,n)
		elif type(n) == type(0):
			self[(('_',0),)] = n
		elif type(n) == type(""):
			self[((n,1),)] = 1
		constant = 0
		for monomial in self.keys():
			exponent = True
			for var in monomial:
				if var[0] == '_':
					exponent = False
					break
				if var[1] != 0:
					exponent = False
					break
			if exponent:
				self.pop(monomial)
				constant += self[monomial]
		if (('_',0),) in self.keys():
			self[(('_',0),)] += constant
		else:
			self[(('_',0),)] = constant
	def __add__(self,p1):
		return polynomial_add(self,p1)
	def __sub__(self,p1):
		return polynomial_add(self,p1*Polynomial(-1))
	def __mul__(self,p1):
		return polynomial_multiply(self,p1)
	def __str__(self):
		return polynomial_str(self)
	def isOne(self):
		if self.keys() == [(('_',0),)]:
			if self[(('_',0),)] == 1:
				return True
		return False
	def isScalar(self):
		if self.keys() == [(('_',0),)]:
			return True
		return False
	def isZero(self):
		if self.key() == []:
			return True
		return False
	def leading(self):
		return sorted(self.keys(),reverse=True)[0]

	

def polynomial_add(p1,p2):
	p3 = Polynomial({})
	for monomial in set(p1).union(set(p2)):
		if monomial in p1 and monomial in p2:
			p3[monomial] = p1[monomial]+p2[monomial]
		elif monomial in p1:
			p3[monomial] = p1[monomial]
		elif monomial in p2:
			p3[monomial] = p2[monomial]
	#check for zeros
	for monomial in p3.keys():
		if p3[monomial] == 0: #get rid of 0 coefs
			p3.pop(monomial)
	return p3

def monomial_multiply(m1,m2):
	hm1= dict(m1)
	hm2= dict(m2)
	result = {}
	for var in set(hm1).union(set(hm2)):
		if var[0] == "_":
			continue #don't tack on scalar 'variable'
		if var in hm2 and var in hm1:
			result[var] = hm1[var]+hm2[var]
		elif var in hm1:
			result[var] = hm1[var]
		else:
			result[var] = hm2[var]
	if result.keys() == []:
		return (('_',0),)
	return tuple(sorted(result.items())) #sort is important

def polynomial_multiply(p1,p2):
	result = []
	for m1 in p1:
		for m2 in p2:
			result.append(
				Polynomial({monomial_multiply(m1,m2):
					p1[m1]*p2[m2]}))
	result = reduce(polynomial_add,result[1:],result[0])
	return result

def monomial_str(m1):
	result = ""
	for var in m1:
		result += var[0]
		if var[1] != 1:
			result += str(var[1])
	return result

def polynomial_str(p1):
	result = []
	if p1.keys()==[]:
		return "0"
	for monomial in sorted(p1.keys()):
		if monomial[0][0] == '_':
			result.append(str(p1[monomial]))
			continue
		m_str = monomial_str(monomial)
		if p1[monomial] != 1:
			m_str = str(p1[monomial])+"*"+m_str
		result.append(m_str)
	return "+".join(result)

def monomial_divide(m1,m2):
	result = []
	print m1
	hm1 = dict(m1)
	hm2 = dict(m2)
	result = {}
	print "monomial dicts:",hm1,hm2
	for var in hm2:
		if var not in hm2 or hm2[var] > hm1[var]:
			print var not in hm2
			return 0
		result[var] = hm1[var]-hm2[var]
	return tuple(sorted(result.items(),reverse=True))
		
		

def polynomial_divide(p1,p2):
	leading1 = p1.leading()
	leading2 = p2.leading()
	quotient = Polynomial(0)
	remainder = Polynomial(p1)
	quotient_term=monomial_divide(leading1,leading2)
	if quotient_term != 0 and remainder.isZero != 0:
		print remainder
		quotient_coef = remainder[leading1]/p2[leading2]
		quotient2 = Polynomial({quotient_term: quotient_coef})

		quotient= quotient + quotient2
		remainder = remainder - quotient2*p2
		leading1 = remainder.leading()
		quotient_term =monomial_divide(leading1,leading2)

	return quotient,remainder

if __name__ =="__main__":	
	while True:
		print "1?",
		p1 = eval(raw_input())
		print map(str,p1)

