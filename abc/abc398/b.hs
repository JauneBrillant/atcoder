import Data.List
import Data.Map.Strict qualified as M

main :: IO ()
main = do
  as <- getInts
  let combs = combinations 5 as
  printYn $ any fullHouse combs

combinations :: Int -> [a] -> [[a]]
combinations 0 _ = [[]]
combinations _ [] = []
combinations n (x : xs) =
  map (x :) (combinations (n - 1) xs) ++ combinations n xs

fullHouse :: (Ord a) => [a] -> Bool
fullHouse hand = do
  let ranksCnt = M.fromListWith (+) [(r, 1) | r <- hand]
   in elem 3 (M.elems ranksCnt) && elem 2 (M.elems ranksCnt)

getInts :: IO [Int]
getInts = map read . words <$> getLine

printYn :: Bool -> IO ()
printYn b = do
  if b then putStrLn "Yes" else putStrLn "No"
