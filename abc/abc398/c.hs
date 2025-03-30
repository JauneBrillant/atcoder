import Data.List
import Data.Map.Strict qualified as Map
import Data.Maybe

main :: IO ()
main = do
  n <- getInt
  as <- getInts

  let uniqueNums = [k | (k, v) <- Map.toList (Map.fromListWith (+) [(a, 1) | a <- as]), v == 1]
  let res = fromMaybe (-1) (safeMax uniqueNums >>= \maxNum -> (+ 1) <$> elemIndex maxNum as)
  print res

safeMax :: (Ord a) => [a] -> Maybe a
safeMax [] = Nothing
safeMax xs = Just (maximum xs)

getInt :: IO Int
getInt = read <$> getLine

getInts :: IO [Int]
getInts = map read . words <$> getLine
