import Data.List qualified as List
import Data.Map.Strict qualified as Map
import Data.Ord (Down (..))
import Data.Set qualified as Set

main :: IO ()
main = do
  n <- getInt
  p <- getInts

  let sortedPCnt = List.sortOn (Down . fst) $ Map.toList $ Map.fromListWith (+) [(x, 1) | x <- p]
  let rankMap = createRankMap sortedPCnt 1 Map.empty
  let result = map (\score -> Map.findWithDefault 0 score rankMap) p
  mapM_ print result

createRankMap :: [(Int, Int)] -> Int -> Map.Map Int Int -> Map.Map Int Int
createRankMap [] _ rankMap = rankMap
createRankMap ((score, count) : rest) currentRank rankMap =
  let newRankMap = Map.insert score currentRank rankMap
   in createRankMap rest (currentRank + count) newRankMap

getInt :: IO Int
getInt = read <$> getLine

getInts :: IO [Int]
getInts = map read . words <$> getLine
