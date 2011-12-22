import System( getArgs )

increment (p1:[]) = [[p1+1]]    --Increment if singleton
increment (p1:(p2:ps))          --Increment if the second is greater than the first
    | p1<p2 = [(p1+1):(p2:ps)]
increment p = []                --Don't create a new one, there will be only one succssor

partition_successor p = [([1]++p)] ++ (increment p)    --Insert 1 to partition, and maybe also increment

partitions :: Num a=>Ord a => a -> [[a]]
partitions 0 = [[]]
partitions n = concat $ map partition_successor (partitions (n-1))

main = do 
        args <- getArgs
        let n = (read (head args) :: Int)
        let k = partitions n
        putStrLn $ show (length k)
        
