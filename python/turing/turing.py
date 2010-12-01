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
tm = TuringMachine({	
'q0':{	'a':('q1','X','R'),
	'Y':('q4','Y','R')},
'q1':{	'a':('q1','a','R'),
	'b':('q2','Y','R'),
	'Y':('q1','Y','R')},
'q2':{	'b':('q2','b','R'),
	'c':('q3','Z','L'),
	'Z':('q2','Z','R')},
'q3':{	'a':('q3','a','L'),
	'b':('q3','b','L'),
	'X':('q0','X','R'),
	'Y':('q0','Y','L'),
	'Z':('q0','Z','L')},
'q4':{	'Y':('q4','Y','R'),
	'Z':('q4','Z','R'),
	'B':('q5','B','R')},
'q5':{}},'q0', ['q5'])

tmVarvel = TuringMachine({
'q0':{	'a':('q1','X','R'),
	'Y':('q4','Y','R')},
'q1':{	'a':('q1','a','R'),
	'b':('q2','Y','R'),
	'Y':('q1','Y','R'),
	'Z':('q1','Z','R')},
'q2':{	'b':('q2','B','R'),
	'c':('q3','Z','L'),
	'Z':('q2','Z','R')},
'q3':{	'a':('q3','a','L'),
	'b':('q3','b','L'),
	'X':('q0','X','R'),
	'Y':('q3','Y','L'),
	'Z':('q3','Z','L')},
'q4':{	'Y':('q4','Y','R'),
	'Z':('q4','Z','R'),
	'B':('q5','B','R')},
'q5':{}},'q0',['q5'])
tmSumit= TuringMachine({
'q0':{	'a':('q1','X','R'),
	'Y':('q0','Y','R'),
	'Z':('q0','Z','R'),
	'B':('q4','B','R')},
'q1':{	'a':('q1','a','R'),
	'b':('q2','Y','R'),
	'Y':('q1','Y','R')},
'q2':{	'b':('q2','b','R'),
	'c':('q3','Z','L'),
	'Z':('q2','Z','R')},
'q3':{	'a':('q3','a','L'),
	'b':('q3','b','L'),
	'X':('q0','X','R'),
	'Y':('q3','Y','L'),
	'Z':('q3','Z','L')},
'q4':{}},'q0',['q4'])

tmSamii=TuringMachine({
'q0':{	'a':('q1','X','R'),
	'Y':('q0','Y','R'),
	'Z':('q0','Z','R'),
	'B':('q4','B','R')},
'q1':{	'a':('q1','a','R'),
	'b':('q2','Y','R'),
	'Y':('q1','Y','R')},
'q2':{	'b':('q2','b','R'),
	'c':('q3','Z','L'),
	'Z':('q2','Z','R')},
'q3':{	'a':('q3','a','L'),
	'b':('q3','b','L'),
	'X':('q0','X','R'),
	'Y':('q3','Y','L'),
	'Z':('q3','Z','L')},
'q4':{}},'q0',['q4'])
tmSamii2=TuringMachine({
'q0':{	'a':('q1','X','R'),
	'b':('q0','b','L'),
	'c':('q0','c','L'),
	'X':('q0','X','R'),
	'Y':('q0','Y','R'),
	'Z':('q3','Z','R')},
'q1':{	'a':('q1','a','R'),
	'b':('q2','Y','R'),
	'X':('q0','X','L'),
	'Y':('q1','Y','L')},
'q2':{	'b':('q2','b','R'),
	'c':('q0','c','L'),
	'Y':('q1','X','L'),
	'Z':('q2','Z','L')},
'q3':{	'Z':('q3','Z','R'),
	'B':('q4','B','R')},
'q4':{}},'q0',['q4'])

tmLong = TuringMachine({
'q0':{	'a':('q1','X','R'),
	'X':('q4','Y','R'),
	'Y':('q4','Y','R')},
'q1':{	'a':('q1','a','R'),
	'b':('q2','Y','R'),
	'Y':('q1','Y','R'),
	'X':('q1','Y','R')},
'q2':{	'b':('q2','b','R'),
	'c':('q3','Z','L'),
	'Z':('q2','Z','R')},
'q3':{	'a':('q3','a','L'),
	'b':('q3','b','L'),
	'X':('q3','Y','L'),
	'Y':('q3','Y','L'),
	'Z':('q3','Z','L')},
'q4':{	'X':('q4','Y','R'),
	'Y':('q4','Y','R'),
	'Z':('q4','Y','R'),
	'B':('q5','B','R')},
'q5':{}},'q0',['q5'])

tmThiara=TuringMachine({
'q0':{	'a':('q1','X','R'),
	'Y':('q4','Y','R')},
'q1':{	'a':('q1','a','R'),
	'b':('q2','Y','R'),
	'Y':('q1','Y','R')},
'q2':{	'b':('q2','b','R'),
	'c':('q3','Z','L'),
	'Z':('q2','Z','R')},
'q3':{	'a':('q3','a','L'),
	'b':('q3','b','L'),
	'X':('q0','X','R'),
	'Y':('q3','Y','L'),
	'Z':('q3','Z','L')},
'q4':{	'Y':('q4','Y','R'),
	'Z':('q5','Y','R')}, 
'q5':{	'Z':('q5','Z','R'),
	'B':('q6','B','R')},
'q6':{}},'q0',['q6'])

tmSelf= TuringMachine({
'q0':{	'a':('q1','X','R'),
	'Y':('q4','Y','R')},
'q1':{	'a':('q1','a','R'),
	'b':('q2','Y','R'),
	'Y':('q1','Y','R')},
'q2':{	'b':('q2','B','R'),
	'c':('q3','Z','L'),
	'Z':('q2','Z','R')},
'q3':{	'a':('q3','a','L'),
	'b':('q3','b','L'),
	'X':('q0','X','R'),
	'Y':('q3','Y','L'),
	'Z':('q3','Z','L')},
'q4':{	'Y':('q4','Y','R'),
	'Z':('q4','Z','R'),
	'B':('q5','B','R')},
'q5':{}},'q0',['q5'])

tmDunn = TuringMachine({
'q0':{	'a':('q1','X','R'),
	'X':('q4','Y','R')},
'q1':{	'a':('q1','a','R'),
	'b':('q2','Y','R'),
	'Y':('q1','Y','R')},
'q2':{	'b':('q2','b','R'),
	'c':('q3','Z','L'),
	'Z':('q2','Z','R')},
'q3':{	'c':('q3','c','R'),
	'B':('q4','B','L')},
'q4':{	'a':('q5','a','L'),
	'b':('q5','b','L'),
	'c':('q5','b','L'),
	'X':('q5','X','L'),
	'Y':('q5','Y','L'),
	'Z':('q5','Y','L'),
	'B':('q4','B','L')},
'q5':{	'a':('q5','a','L'),
	'b':('q5','b','L'),
	'c':('q5','b','L'),
	'X':('q5','X','L'),
	'Y':('q5','Y','L'),
	'Z':('q5','Y','L'),
	'B':('q4','B','R')},
'q6':{}},'q0',['q6'])
tmKominsky = TuringMachine({
'q0':{	'a':('q1','X','R'),
	'Y':('q4','Y','R')},
'q1':{	'a':('q1','a','R'),
	'b':('q2','Y','R'),
	'Y':('q1','Y','R')},
'q2':{	'b':('q2','b','R'),
	'c':('q3','Z','L'),
	'Z':('q2','Z','R')},
'q3':{	'a':('q3','a','L'),
	'b':('q3','b','L'),
	'X':('q0','X','R'),
	'Y':('q3','Y','L'),
	'Z':('q3','Z','L')},
'q4':{	'Y':('q4','Y','R'),
	'Z':('q5','Y','R')}, 
'q5':{	'Z':('q5','Z','R'),
	'B':('q6','B','R')},
'q6':{}},'q0',['q6'])
tmChu= TuringMachine({
'q':{	'a':('[a,bc]','X','R'),
	'X':('q','X','R'),
	'B':('f','B','R')},
'[a,bc]':{
	'a':('[a,bc]','a','R'),
	'b':('[ab,c]','X','R'),
	'X':('[a,bc]','X','R')},
'[ab,c]':{
	'b':('[ab,c]','b','R'),
	'c':('s','X','L'),
	'X':('[ab,c]','X','R')},
's':{	'a':('s','a','L'),
	'b':('s','b','L'),
	'X':('s','X','L'),
	'B':('q','B','R')},
'f':{}},'q',['f'])
tmRhodes=TuringMachine({
'q0':{	'a':('q1','X','R')},
'q1':{	'a':('q1','a','R'),
	'b':('q2','X','R')},
'q2':{	'b':('q2','b','R'),
	'c':('q3','X','L'),
	'X':('q2','X','R')},
'q3':{	'a':('q4','X','R'),
	'b':('q3','b','L'),
	'X':('q3','X','L'),
	'B':('q5','B','R')},
'q4':{	'b':('q2','X','R'),
	'X':('q4','X','R')}, 
'q5':{	'X':('q5','X','R'),
	'B':('q6','B','R')},
'q6':{}},'q0',['q6'])
tmWolfe= TuringMachine({
'q0':{	'a':('q1','X','R')},
'q1':{	'a':('q1','a','R'),
	'b':('q2','Y','R'),
	'Y':('q2','Y','R')},
'q2':{	'b':('q2','b','R'),
	'c':('q3','Z','L'),
	'Z':('q2','Z','R')},
'q3':{	'a':('q3','a','L'),
	'b':('q3','b','L'),
	'X':('q0','X','R'),
	'Y':('q3','Y','L'),
	'Z':('q3','Z','L')},
'q4':{}},'q0',['q4'])
tmHagen=TuringMachine({
'q0':{	'a':('q1','X','R'),
	'X':('q5','X','R')},
'q1':{	'a':('q1','a','R'),
	'b':('q2','Y','R')},
'q2':{	'b':('q2','b','R'),
	'c':('q3','Z','R')},
'q3':{	'c':('q3','c','R'),
	'B':('q4','B','L')},
'q4':{	'a':('q4','a','L'),
	'b':('q4','b','L'),
	'c':('q4','c','L'),
	'X':('q4','X','L'),
	'Y':('q4','Y','L'),
	'Z':('q4','Z','L'),
	'B':('q0','B','R')},
'q5':{	'a':('q1','a','R'),
	'X':('q5','X','R'),
	'Y':('q6','Y','R')},
'q6':{	'b':('q2','b','R'),
	'Y':('q6','Y','R'),
	'Z':('q7','Z','R')},
'q7':{	'c':('q3','b','R'),
	'Z':('q7','b','R'),
	'B':('q8','B','L')},
'q8':{	'Y':('q9','Y','L'),
	'Z':('q8','Z','L')},
'q9':{	'X':('q10','X','L'),
	'Y':('q9','Y','L')},
'q10':{	'X':('q10','X','L'),
	'B':('q11','B','L')},
'q11':{}},'q0',['q11'])

bob = TuringMachine({	'q0':{'a':('q1','a','R')},
			'q1':{'a':('q0','a','R'),
			      'B':('q2','B','L')},
			'q2':{'a':('q2','b','L')}
		    },'q0',['q2'])

bob = tmChu

while True:
	bob.check(raw_input().strip())
