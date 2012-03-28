import Text.Regex.Posix

data ASTree = Number Int | Binop Operator ASTree ASTree | Empty deriving Show
data Operator = Plus | Mult | Div | Sub | Exp deriving Show
data Group = ParenLeft | ParenRight deriving Show
data Token = TokenO Operator | TokenN Int | TokenG Group deriving Show


buildToken x | x =~ "[0-9]+" = TokenN (read x :: Int)
             | x == "(" = TokenG ParenLeft
             | x == ")" = TokenG ParenRight
             | x == "+" = TokenO Plus
             | x == "/" = TokenO Div
             | x == "*" = TokenO Mult
             | x == "-" = TokenO Sub
             | x == "^" = TokenO Exp

buildTree :: [Token] -> ASTree -> ASTree


--Non-Exhaustive, but all correctly formatted inputs should pass.
buildTree [] left = left
buildTree ((TokenN x):xs) Empty = buildTree xs (Number x)
buildTree ((TokenO op):xs) left = Binop op left (buildTree xs Empty)
buildTree ((TokenG ParenLeft):xs) Empty = buildTree xs Empty
buildTree ((TokenG ParenRight):xs) left = left


opChar Div = "/"
opChar Mult = "*"
opChar Sub = "-"
opChar Plus = "+"
opChar Exp = "^"

postOrderTraversal (Number x) = show x
postOrderTraversal (Empty) = "Empty"
postOrderTraversal (Binop op left right) = (postOrderTraversal left) ++ 
                                           (postOrderTraversal right) ++
                                           (opChar op) 


tokenize :: String -> [Token]
tokenize x = let list = (preprocess x) in
                map buildToken list
		
preprocess x = getAllTextMatches $ 
                x =~ "([0-9]+|\\(|\\)|[\\+-\\*\\/^])" :: [String]

main = do 
    line <- getLine
    putStrLn $ show $ buildTree (tokenize line) Empty
    putStrLn $ postOrderTraversal $ buildTree (tokenize line) Empty
    main
