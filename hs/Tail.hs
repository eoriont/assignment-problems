tail' :: (Num a, Ord a) => a -> [a] -> [a]
tail' n x = reverseList (take' n (reverseList x))

reverseList :: [a] -> [a]
reverseList [] = []
reverseList (x : xs) = reverseList xs ++ [x]

take' :: (Num i, Ord i) => i -> [a] -> [a]
take' n _
  | n <= 0 = []
take' _ [] = []
take' n (x : xs) = x : take' (n -1) xs

main = print (tail' 4 [8, 3, -1, 2, -5, 7])
