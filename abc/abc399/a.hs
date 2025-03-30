main :: IO ()
main = do
  n <- getInt
  s <- getLine
  t <- getLine

  let res = length $ [1 | (x, y) <- zip s t, x /= y]
  print res

getInt :: IO Int
getInt = read <$> getLine
