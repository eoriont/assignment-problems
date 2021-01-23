recommendClothing :: (RealFloat a) => a -> String
recommendClothing degreesCelsius
  | degreesFarenheit >= 80 = "shortsleeve shirt"
  | 80 > degreesFarenheit && degreesFarenheit > 65 = "longsleeve shirt"
  | 65 > degreesFarenheit && degreesFarenheit > 50 = "sweater"
  | otherwise = "jacket"
  where
    degreesFarenheit = degreesCelsius * 9 / 5 + 32
