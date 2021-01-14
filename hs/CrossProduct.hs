crossProduct :: (Num a) => (a, a, a) -> (a, a, a) -> (a, a, a)
crossProduct (x1, y1, z1) (x2, y2, z2) = (y1 * z2 - z1 * y2, z1 * x2 - x1 * z2, x1 * y2 - y1 * x2)

main = print (crossProduct (1, 2, 3) (3, 2, 1))
