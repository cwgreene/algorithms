from polynomial import Polynomial,pgcd,polynomial_divide

class RationalExpression(object):
	def __init__(self,p1,p2=None):
		if not isinstance(p1,Polynomial):
			raise "Scream and yell"
		if p2==None:
			p2 = Polynomial(1)
		common = pgcd(p1,p2)
		self.numerator=polynomial_divide(p1,common)[0]
		self.denominator=polynomial_divide(p2,common)[0]
	def __mul__(self,e2):
		return RationalExpression(self.numerator*e2.numerator,
					  self.denominator*e2.denominator)
	def __add__(self,e2):
		num = (e2.numerator*self.denominator+
				self.numerator*e2.denominator)
		denom = e2.denominator*self.denominator
		return RationalExpression(num,denom)
	#i'm going to regret this
	def __sub__(self,e2):
		num =(self.numerator*e2.denominator-
				e2.numerator*self.denominator) 
		denom = e2.denominator*self.denominator
		return RationalExpression(num,denom)
	def __div__(self,e2):
		num = self.numerator*e2.denominator
		denom = self.denominator*e2.numerator
		return RationalExpression(num,denom)
	def __str__(self):
		result =""
		if self.denominator.isOne():
			return str(self.numerator)
		if self.numerator.isScalar():
			result += str(self.numerator)
		else:
			result += "("+str(self.numerator)+")"
		result += "/"
		if self.denominator.isScalar():
			result += str(self.denominator)
		else:
			result += "("+str(self.denominator)+")"
		return result
