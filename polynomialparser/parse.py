import re
import sys
import options
import readline

from polynomial import Polynomial
from rational_expression import RationalExpression

def try_match(pattern,target,success_token,token_list):
	match = re.match(pattern,target)
	if match:
		token_list.append((success_token,match.group()))
		return target[match.end():]
	return target

def parse(string):
	token_list = []
	remaining = string
	#cheating, assuming valid input for now
	#since it says the input is highly restricted
	#assuming valid
	while remaining != "":
		remaining = remaining.strip() #kill space
		remaining = try_match("^[0-9]+",remaining,
				"NUMBER",token_list)
		remaining = try_match("^[\+\-\*\/\^]",remaining,
				"OPERATOR",token_list)
		remaining = try_match("^[a-zA-Z]",remaining,
				"SYMBOL",token_list)
		remaining = try_match("^\(",remaining,
				"START_GROUP",token_list)
		remaining = try_match("^\)",remaining,
				"END_GROUP",token_list)
	return token_list

def tok_type(token):
	return token[0]
def tok_val(token):
	return token[1]

all_symbols = set()
def ast_atom(token_list):
	cur_token = token_list[0]
	if tok_type(cur_token) == "NUMBER":
		return cur_token,token_list[1:]
	if tok_type(cur_token) == "SYMBOL":
		symbol = tok_val(cur_token)
		all_symbols.add(symbol)
		return cur_token,token_list[1:]
	if tok_type(cur_token) in ["START_GROUP"]:
		expr,rem = ast_expr(token_list[1:])	
		#consume END_GROUP
		return expr,rem[1:]
	

def ast_term(token_list):
	cur_token = token_list[0]
	if tok_type(cur_token) in ["START_GROUP","NUMBER","SYMBOL"]:
		term,rem=ast_atom(token_list)
		if rem == []:
			return term,rem
		if tok_val(rem[0]) in "+-)":#end of term
			return term,rem
		while rem != [] and tok_val(rem[0]) in "*/^":
			operator = rem[0]
			atom,rem = ast_atom(rem[1:])
			term = [operator,[term,atom]]
		return term,rem

def ast_expr(token_list):
	"""
	expr-> expr,"+",term | expr,"-",term
	expr-> term
	term-> atom | term,"*",atom | term ,"/",atom | term ,"^", atom
	atom-> group | NUMBER | SYMBOL
	group-> START_GROUP,expr,END_GROUP
	"""
	if token_list == []:
		return [],[]
	cur_token = token_list[0]
	term,rem = ast_term(token_list)
	expr = term
	while rem != [] and tok_type(rem[0]) != "END_GROUP":
		if tok_type(rem[0])=="OPERATOR": #must be +/-
			operator=rem[0]
		term,rem = ast_term(rem[1:])
		expr = [operator,[expr,term]]
	return expr,rem
	raise "Not Expression"

def print_tree(tree,depth=0):
	if type(tree) == type([]):
		head = tree[0]
		print_tree(head,depth+1)
		print_tree(tree[1][0],depth+2)
		print_tree(tree[1][1],depth+2)
	else:
		print " "*depth,tok_val(tree)

def lisp_tree_str(tree):
	result = ""
	if type(tree) == type([]):
		head = tree[0]
		return "(%s %s %s)"% (head[1],
					lisp_tree_str(tree[1][0]),
					lisp_tree_str(tree[1][1]))
	else:
		return tree[1]

def reduce_tree(tree):
	if type(tree) == type([]):
		head = tree[0]
		operator = head[1]
		left = reduce_tree(tree[1][0])
		right = reduce_tree(tree[1][1])
		if tok_type(left)==tok_type(right)=="NUMBER":
			return ("NUMBER",eval(left[1]+operator+right[1]))
	return tree

def polynomial_tree(tree):
	if type(tree) == type([]):
		head = tree[0]
		left = polynomial_tree(tree[1][0])
		right = polynomial_tree(tree[1][1])
		return [head,[left,right]]
	#at a node
	token = tree
	if tok_type(token) == "NUMBER":
		return ("POLYNOMIAL",RationalExpression(Polynomial(int(tok_val(token)))))
	if tok_type(token) == "SYMBOL":
		return ("POLYNOMIAL",RationalExpression(Polynomial(tok_val(token))))
	return tree

def reduce_poly(poly_tree):
	if type(poly_tree) == type([]):
		head = poly_tree[0]
		operator = head[1]
		left = reduce_poly(poly_tree[1][0])
		right = reduce_poly(poly_tree[1][1]) # This means that right is always RE
		if operator == '+':
			return ("POLYNOMIAL",left[1]+right[1])
		elif operator == '*':
			return ("POLYNOMIAL",left[1]*right[1])
		elif operator == '-':
			return ("POLYNOMIAL",left[1]-right[1])
		elif operator == '/':#polynomial is a lie
			return ("POLYNOMIAL",left[1]/right[1])
		elif operator == '^':
			if not right[1].isScalar():
				raise Exception("Only Integer Exponents supported")
			repeat = right[1].scalar()
			acc = RationalExpression(Polynomial(1))
			for i in range(repeat):
				acc = acc*left[1]
			return ("POLYNOMIAL", acc)
	else:
		return ("POLYNOMIAL",poly_tree[1])

def eval_expression(expression,eval,destination,options):
	parsed = parse(expression)
	tree = ast_expr(parsed)
	result = ""
	if eval:
		poly_tree = polynomial_tree(tree[0])
		poly = reduce_poly(poly_tree)
		if options.lisp:
		    result = poly[1].lisp_str()
		else:
			result = poly[1]
	else:
 		if options.lisp:
		    result = lisp_tree_str(tree[0])
		else:
			result = tree[0]
	print>>destination,result

class ReadlineWrap(object):
    def readline(self):
        return raw_input()

def main(options,args):
	destination = sys.stdout
	if options.expression != None:
		eval_expression(options.expression,options.eval,destination)
		return
	if options.filename:
		input_file = open(options.filename)
	else:
		input_file = ReadlineWrap()
	while True:
		try:		
			input = input_file.readline().strip()
			if input == "":
				break
			eval_expression(input,options.eval,destination,options)
			
		except EOFError:
			break
if __name__=="__main__":
	options,args = options.parse_options(sys.argv)
	main(options,args)
