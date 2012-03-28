import optparse

def parse_options(args):
	parser = optparse.OptionParser()
	parser.add_option("-x",dest="expression",
			help="directly evaluate expression",
			default=None)
	parser.add_option("-f",dest="filename",
			help="filename containing list of expressions "+
			"if not specified, STDIN is used",
			default=None)
	parser.add_option("-e",action="store_true",dest="eval",default=False,
			help="Evaluation switch, default is off")
	parser.add_option("-l",action="store_false",dest="lisp",default=True,
            help="Do not display in lisp form")
	options,args = parser.parse_args()
	return options,args
