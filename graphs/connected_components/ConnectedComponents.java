/*Problem with java, this should really just be a method inside
 * of a larger graph class*/
import java.util.*;
class ConnectedComponents
{
	static int MARKER = 'X';
	static int OPEN = '.';
	public static void findcomponent( int[][] graph, 
					int x, int y,
					HashSet<Integer> set) {
		set.add(y*graph.length+x);
		graph[x][y] = MARKER;
		if(x != 0 && graph[x-1][y] == OPEN)
		{
			findcomponent(graph,x-1,y,set);
		}
		if(x+1 < graph[y].length && graph[x+1][y] == OPEN)
		{
			findcomponent(graph,x+1,y,set);
		}
		if(y != 0 && graph[x][y-1] == OPEN)
		{
			findcomponent(graph,x,y-1,set);
		}
		if(y +1 < graph.length && graph[x][y+1] == OPEN)
		{
			findcomponent(graph,x,y+1,set);
		}
	}
	public static Vector<HashSet<Integer>> findcomponents(int[][] graph)
	{
		Vector<HashSet<Integer>> result = new 
			Vector<HashSet<Integer>>();
		for(int i =0; i < graph.length;i++)
		{
			for(int j=0; j < graph[i].length;j++)
			{
				if(graph[i][j] == OPEN)
				{
					HashSet<Integer> set = 
						new HashSet<Integer>();
					findcomponent(graph,i,j,set);
					result.add(set);
				}
			}
		}
		return result;
	}
}
