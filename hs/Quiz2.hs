calcGPA x = fromIntegral (sum (map gradeToNumber x)) / fromIntegral (length x)

gradeToNumber x
  | x == "A" = 4
  | x == "B" = 3
  | x == "C" = 2
  | x == "D" = 1
  | x == "F" = 0

main = print (calcGPA ["A", "B", "B", "C", "C", "C", "D", "F"])
