classifyNumber x
  | x > 0 = "nonnegative" -- or positive lol
  | x == 0 = "zero"
  | otherwise = "negative"

main = putStrLn (classifyNumber 5)
