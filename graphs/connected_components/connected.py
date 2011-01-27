import sys

class Graph:
	def __init__(self):
		self.nodes = set()
		self.edges = set()
		self.properties = []
	def __repr__(self):
		str = "nodes: "+repr(self.nodes)+"\n"
		str += "edges: "+repr(self.edges)+"\n"
		str += repr(self.properties)
		return str

def connected_components_set(graph):
	collections = set()
	marked = set()
	def connected_component(graph,node):
		collection = set([node])
		for a,b in graph.edges:
			if a in collection:
				collection.add(b)
		return collection
	for node in graph.nodes:
		if node in marked:
			continue
		next = connected_component(graph,node)
		collections.add(tuple(next))
		marked.union(collections)
	return collections

def parse_file_set(filename):
	file = open(filename)
	graph = Graph()
	for line in file:
		line = line.strip()
		if line in ["undirected"]:
			graph.properties.append("undirected")
			continue
		a,b = line.split()
		graph.nodes= graph.nodes.union([a,b])
		graph.edges.add((a,b))
	if "undirected" in graph.properties:
		closure = set()
		for a,b in graph.edges:
			closure.add((b,a))
	graph.edges = graph.edges.union(closure)
	print graph
	return graph


def main(args):
	if len(args) < 1:
		print "file name expected"
		exit()
	filename = args[0]
	graph = parse_file_set(filename)
	print connected_components_set(graph)

if __name__=='__main__':
	main(sys.argv[1:])
