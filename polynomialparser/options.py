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
	options,args = parser.parse_args()
	return options,args
