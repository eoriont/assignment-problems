merge (x : xs) (y : ys) =
  if x < y
    then x : merge xs (y : ys)
    else y : merge (x : xs) ys
merge [] xs = xs
merge xs [] = xs

main = print (merge [1, 2, 5, 8] [3, 4, 6, 7, 10])

-- should return [1,2,3,4,5,6,7,8,10]
