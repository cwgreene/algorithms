class TuringMachine:
	#example transition dict:
	#trans = {'q0':{'a':('a','R')}}
	def __init__(self,transitions,start,accept):
		self.transitions = transitions	
		self.start = start
		self.accept = accept

	def valid_trans(self,symbol,current_state):
		return symbol in self.transitions[current_state]
			
	def check(self,input,max=1000):
		input = input
		current_state = self.start
		tape = list(input)
		position = 0
		steps = 0
		try:
			while (self.valid_trans(tape[position],
						current_state)
					and steps < max):
				print current_state,("".join((tape[0:position]))
					+"*"+
					"".join(tape[position:])),
				steps += 1
				trans = self.transitions[current_state]\
							[tape[position]]
				print tape[position],trans
				current_state = trans[0]
				tape[position] = trans[1]
				if trans[2] == 'R':
					position += 1
					if position >= len(tape):
						tape.append("B")
				elif trans[2] == 'L':
					position -= 1
					if position < 0:
						tape.insert(0,'B')
						position = 0
				else:
					print "Invalid Direction"
					return
		except Exception,E:
			print "Exception:",current_state,E,type(E)
		print current_state,("".join(tape[0:position])
					+"*"+
					"".join(tape[position:]))
		if current_state in self.accept:
			print "In accept state in",steps,current_state
		else:
			print "Not accepted in",steps
		return

