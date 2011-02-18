{-Problem 1-}
myLast [] = error "Last element of empty list is undefined"
myLast (x:[]) = x
myLast (x:xs) = myLast xs

{-Problem 2-}
listTooShort = "List too short"

myButLast x = if length x < 2 
			then error listTooShort
			else case x of
				(x:y:[]) -> x
				(x:xs) -> myButLast xs
-- Alt
myButLast' x = if length x < 2
			then error listTooShort
			else myButLastSafe' x
myButLastSafe' (x:y:[]) = x
myButLastSafe' (x:xs) = myButLastSafe' xs

{-Problem 3-}
elementAt x n = x !! (n-1)

elementAt' (x:xs) 1 = x
elementAt' (x:xs) n = elementAt' xs (n-1)

{-Problem 4-}
myLength x = myLength' x 0 where
		myLength' [] n = n
		myLength' (x:xs) n = myLength' xs (n+1)

myLength' x = length x
{-Problem 5-}
myreverse [] = []
myreverse (x:xs) = (myreverse xs)++[x]

{-Problem 6-}
isPalindrome x = myreverse x == x

{-Problem 7-}
data NestedList a = Elem a | List [NestedList a]

flatten:: NestedList a -> [a]
flatten (Elem x) = [x]
flatten (List []) = []
flatten (List (x:xs)) = flatten x ++ flatten (List xs)

{-Problem 8-}
compress [] = []
compress (x:xs) = compress' xs x [x] where
			compress' [] last acc = acc
			compress' (x:xs) last acc = 
				if x == last
					then compress' xs last acc
					else compress' xs x (acc++[x])

{-Problem 9-}
pack :: Eq a => [a] -> [[a]]
pack [] = []
pack (x:xs) = foldl (\a b-> 
			if head (last a) == b
			 then (init a) ++ [((last a)++[b])]
			 else a ++ [[b]]) 
			[[x]] xs

{-Problem 10-}
encode x = map (\a -> (length a, head a)) (pack x)

{-Problem 11-}
data Encoding a = Multiple Int a | Single a deriving (Eq, Show)
encodeModified x = map (\x -> countpair x) (pack x) where
			countpair a = if length a == 1
					then Single (head a)
					else Multiple (length a) (head a)

{-Problem 12-}
decodeModified :: [Encoding a] -> [a]
decodeModified [] = []
decodeModified (x:xs) = decode x ++ decodeModified xs where
				decode (Single a) = [a]
				decode (Multiple i a) = replicate i a
{-Problem 13-}
{-This is ugly, but the solutions
 - online don't seem all that much better. Hm.-}
encodeDirect [] = []
encodeDirect (x:xs) = encodeDirect' xs x 1 [] where
			encodeDirect' [] lastval lastcount acc =
				acc++[(encode lastval lastcount)]
			encodeDirect' (x:xs) lastval lastcount acc = 
				if lastval == x --Keep going
				 then (encodeDirect' xs 
					lastval (lastcount+1)
					acc)
				 else (encodeDirect' xs 
					x 1 --reset with x
					acc++[(encode lastval lastcount)])
			encode x 1 = Single x
			encode x n = Multiple n x

{-Problem 14-}
dupli [] = []
dupli (x:xs) = x:x:(dupli xs)

{-Problem 15-}
repli:: [a]->Int -> [a]
repli [] n = []
repli (x:xs) n = (replicate n x)++(repli xs n)

{-Problem 16-}
dropEvery:: [a]-> Int -> [a]
dropEvery [] n = []
dropEvery x n = drop' x n n
		where 	drop' [] n count = []
			drop' (x:xs) n 1 = drop' xs n n
			drop' (x:xs) n c = x:(drop' xs n (c-1))

{-Problem 17-}
split:: [a]->Int->([a],[a])
split x n = (firstPart x n,secondPart x n) where
		firstPart [] n = []
		firstPart x 0 = []
		firstPart (x:xs) n = x:(firstPart xs (n-1))
		secondPart x n = myreverse $
				  firstPart (myreverse x) ((myLength x)-n)

{-Problem 18-}
slice :: [a]->Int->Int->[a]
slice x a b = snd $ split (fst (split x b)) (a-1)

{-Problem 19-}
rotate :: [a]->Int->[a]
rotate list n= b++a where
		(a,b) = split list (normalize list n) where
		normalize alist z = z `mod` (length alist)

{-Problem 20-}
removeAt :: Int->[a] -> (a, [a])
removeAt n (x:xs) = removeAt' (x:xs) n [] where
			removeAt' (x:xs) 0 prior = (x, prior++xs)
			removeAt' (x:xs) n prior = 
				(fst $ removeAt' xs (n-1) (prior++[x]), 
				 snd $ removeAt' xs (n-1) (prior++[x]))
