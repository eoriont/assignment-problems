squareSingleDigitNumbers :: (Ord x, Num x) => [x] -> [x]
squareSingleDigitNumbers xs = map (^ 2) (filter (< 10) xs)

main = print (squareSingleDigitNumbers [2, 7, 15, 11, 5])
