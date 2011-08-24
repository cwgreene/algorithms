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
			if self[monomial]==0:
				self.pop(monomial)
				continue
			exponent = True
			m = normalized_monomial(monomial)
			value = self.pop(monomial)
			for var in monomial:
				if var[0] == '_':
					exponent = False
					break
				if var[1] != 0:
					exponent = False
					break
			if exponent:
				constant +=value
			else:
				self[m] = value
		if (('_',0),) in self.keys():
			self[(('_',0),)] += constant
		elif constant != 0:
			self[(('_',0),)] = constant
	def __add__(self,p1):
		return Polynomial(polynomial_add(self,p1))
	def __sub__(self,p1):
		return Polynomial(polynomial_add(self,p1*Polynomial(-1)))
	def __mul__(self,p1):
		return Polynomial(polynomial_multiply(self,p1))
	def __str__(self):
		return polynomial_str(self)
	def __mod__(self,p2):
		quotient,remainder = polynomial_divide(self,p2)
		return remainder

	def lisp_str(self,list=None): #this is way uglier than it should be
		def lisp_monomial(m):
			def lisp_var(v):
				#x^3 -> (* (* x x) x)
				result = ""
				var_name,var_count = v[0],v[1]
				#scalars are special
				if var_name == "_":
					return ""
				#if were at the end, just print var name
				if var_count == 1:
					return var_name
				#otherwise, spit out, and recurse down
				#with reduced exponent
				result += ("(* "+var_name+" "+
						lisp_var((var_name,var_count-1))
						+")")
				return result
			#this case shouldn't happen
			if len(m) == 0:
				return "" 
			#if we have only one variable name, 
			#we just spit out that variable raised to the exponent
			if len(m) == 1:
				return lisp_var(m[0])
			#otherwise, we need to chain multiplication
			#each variable xzy^2->(* x (* z (* y y)))
			else:
				return ("(* "+lisp_var(m[0])+" "+
						lisp_monomial(m[1:])+")")
		#first step: get all monomials
		if list == None:
			list = self.keys()
			if len(list) == 0:
				return "0"
		#handle base case
		if len(list) == 1:
			#scalars are special
			if list[0][0][0] == "_":
				return str(self[list[0]])
			#(* 1 x) should be written simply as x
			if self[list[0]] == 1:
				return lisp_monomial(list[0])
			#okay, handle it otherwise
			else:
				return ("(* "+str(self[list[0]])+ " "+
					lisp_monomial(list[0])+")")
		else:
			#scalars are special
			if list[0][0][0] == "_":
				return("(+ "+str(self[list[0]])+" "+
						self.lisp_str(list[1:])+") ") 
			#again, leading coefficients of one are ignored
			if self[list[0]] == 1:
				return ("(+ "+lisp_monomial(list[0])+" "+
					self.lisp_str(list[1:])+")")
			#normal case 2*x->(* 2 x)
			else:
				return ("(+ "+"(* "+str(self[list[0]])+" "+
						lisp_monomial(list[0])+") "+
						self.lisp_str(list[1:])+") ")
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
		if self.keys() == []:
			return True
		return False
	def leading(self):
		keys = self.keys()
		if keys:
			return sorted(keys,reverse=True)[0]
		return (('_',0),)
	def __cmp__(self,p2):
		if not isinstance(p2,Polynomial):
			return 1
		k1=sorted(self.keys(),reverse=True)
		k2=sorted(p2.keys(),reverse=True)
		k1=map(lambda x: (x,self[x]),k1)
		k2=map(lambda x: (x,p2[x]),k2)
		return cmp(k1,k2)

def normalized_monomial(m):
	result = []
	for var in m:
		if var[1] != 0 or var[0]=="_":
			result.append(var)
	return tuple(result)

def pgcd(p1,p2):
	if p2.isZero():
		return p1
	if p1 < p2:
		return pgcd(p2,p1)
	quotient, remainder = polynomial_divide(p1,p2)
	if quotient.isZero():
		return Polynomial(1)
	return pgcd(p2,remainder)

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
	return tuple(sorted(result.items(),reverse=True)) #sort is important

def polynomial_multiply(p1,p2):
	if p1.isZero() or p2.isZero():
		return Polynomial(0)
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
	if p1.isZero()==[]:
		return "0"
	for monomial in sorted(p1.keys(),reverse=True):
		if monomial[0][0] == '_':
			if p1[monomial] != 0:
				result.append(str(p1[monomial]))
			continue
		m_str = monomial_str(monomial)
		if p1[monomial] != 1:
			m_str = str(p1[monomial])+"*"+m_str
		result.append(m_str)
	return "+".join(result)

def monomial_divide(m1,m2):
	result = []
	hm1 = dict(m1)
	hm2 = dict(m2)
	result = {}
	for var in hm2:
		if var not in hm2 or (var not in hm1) or hm2[var] > hm1[var]:
			return 0
		result[var] = hm1[var]-hm2[var]
	for var in hm1:
		if var not in hm2:
			result[var] = hm1[var]
	return tuple(sorted(result.items(),reverse=True))
		
def poly_scalar_divide(p1,sp):
	result = Polynomial(0)
	if sp.isZero():
		return Polynomial(0)
	scalar = sp.values()[0]
	for monomial in p1:
		result[monomial] = p1[monomial]/scalar
	return Polynomial(result)

def polynomial_divide(p1,p2):
	if p2.isScalar():
		quotient = poly_scalar_divide(p1,p2)
		remainder = p1-quotient*p2
		return quotient,remainder
	leading1 = p1.leading()
	leading2 = p2.leading()
	quotient = Polynomial(0)
	remainder = Polynomial(p1)
	quotient_term=monomial_divide(leading1,leading2)
	while quotient_term != 0 and remainder.isZero() != True:
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
		print p1

