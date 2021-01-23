smallestDistances :: (RealFloat a) => [(a, a, a)] -> [a]
smallestDistances points = [dist | (x, y, z) <- points, let dist = sqrt (x ^ 2 + y ^ 2 + z ^ 2), dist <= 10]

main = print (smallestDistances [(5, 5, 5), (3, 4, 5), (8, 5, 8), (9, 1, 4), (11, 0, 0), (12, 13, 14)])
