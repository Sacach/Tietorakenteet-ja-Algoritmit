# Test function for BFS
from weightedgraph import *

def main():
	g = WeightedGraph(8)
	
	add_edge(g,1,2,4)
	add_edge(g,1,4,7)
	add_edge(g,1,5,3)
	
	add_edge(g,2,3,1)
	add_edge(g,2,4,8)
	
	add_edge(g,3,4,2)
	
	add_edge(g,4,6,2)
	
	add_edge(g,5,6,5)
	
	add_edge(g,6,7,3)
	add_edge(g,6,8,3)

	dijkstra(g,1)
	print('Path from 1 to 8 with cumulative weights:')
	print_path(g,8)	
	
main()