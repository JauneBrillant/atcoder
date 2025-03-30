main :: IO ()
main = do
  n <- readLn :: IO Int

  if even n
    then putStrLn (replicate (n `div` 2 - 1) '-' ++ "==" ++ replicate (n `div` 2 - 1) '-')
    else putStrLn (replicate (n `div` 2) '-' ++ ['='] ++ replicate (n `div` 2) '-')
