import java.util.HashSet;

public class HashTest
{
	static class Pair{
		int first;
		int second;

		Pair(int x,int y)
		{
			first=x;
			second=y;
		}
		public int hashCode()
		{
			return first+second;
		}

		public boolean equals(Object o)
		{
			Pair other = (Pair)o;
			return (first == other.first )
				&& (second==other.second);
		}

		public String toString()
		{
			return	Integer.toString(first)+":"+
				Integer.toString(second);
		}
	}

	public static void main(String[] args)
	{
		HashSet<int[]> set = new HashSet<int[]>();
		int[] one = {1,2};
		int[] two = {1,2};
		set.add(one);
		if(set.contains(two))
		{
			System.out.println("Success!");
		}else
		{
			System.out.println("failure!");
		}
		HashSet<Pair> set2 = new HashSet<Pair>();
		Pair bob = new Pair(4200*1000*1000,4100*1000*1000);
		Pair joe = new Pair(4200*1000*1000,4100*1000*1000);

		System.out.println(bob+ "h: "+bob.hashCode());
		set2.add(bob);
		if(set2.contains(joe))
			System.out.println("Success!");
		else
			System.out.println("Failure!");
	}
}
