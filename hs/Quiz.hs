sumFactors x = sum [a | a <- [1 .. x], x `mod` a == 0]

main = print (sumFactors 10)
