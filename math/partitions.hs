import System( getArgs )

increment (p1:[]) = [[p1+1]]
increment (p1:(p2:ps))
    | p1<p2 = [(p1+1):(p2:ps)]
increment p = []

p_exp p = [([1]++p)] ++ (increment p)

partitions :: Num a=>Ord a => a -> [[a]]
partitions 0 = [[]]
partitions n = concat $ map p_exp (partitions (n-1))

main = do 
        args <- getArgs
        let n = (read (head args) :: Int)
        let k = partitions n
        putStrLn $ show (length k)
        
