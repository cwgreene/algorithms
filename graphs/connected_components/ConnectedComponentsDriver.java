import ConnectedComponents;

class ConnectedComponentsDriver
{
	public static int[][] parsefile(String filename)
	{
		Vector filevec = new Vector()
		FileReader fr = new FileReader(filename);
		char cur = fr.read();
		while(cur != -1)
		{
			filevec = 
			while(cur != '\n')
			{
			}
		}
		int[][] filearray = new int[filevec.size()][];
		for(int i = 0; i < filevec.size();i++)
		{
			filearray[i]filevec
		}
	}
	public static void main(String[] args)
	{
		int[][] graph = parsefile(args[1]);
		ConnectedComponents.findcomponents();
	}
}
