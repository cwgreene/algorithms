import java.util.*;

class Partitions{
    public static List<List<Integer>> partitions(int n){
        List<List<Integer>> partitions = new ArrayList<List<Integer>>();
        if(n<=0){
            partitions.add(new ArrayList<Integer>());
            return partitions;
        }
        List<List<Integer>> prev_partitions = partitions(n-1);
        int ppsize=prev_partitions.size();
        for(int i = 0; i < ppsize;i++){
        	List<Integer> p = prev_partitions.get(i);
            List<Integer> a = new ArrayList<Integer>();
            a.add(1);
            a.addAll(p);
            partitions.add(a);
            
            int psize = p.size();
            if(psize != 0)
            {
            	if( (psize < 2) || (p.get(1) > p.get(0))){
	            	List<Integer> b = new ArrayList<Integer>();
	            	b.add(p.get(0)+1);
	            	b.addAll(p.subList(1,psize));
	            	partitions.add(b);
            	}
            }
        }
        return partitions;
    }

    public static void main(String[] args){
        List<List<Integer>> partitions= partitions(Integer.parseInt(args[0]));
        System.out.println(partitions.size());
/*        for(List<Integer> partition : partitions){
            for(Integer s : partition){
                System.out.print(s+" ");
            }
            System.out.println();
        }*/
    }
}
