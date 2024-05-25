# prime

## 解法
1. エラトステネスのふるい
2. i * i <= nまで判定 

- 0 != prime
- 1 != prime
- 2 == prime
- 3 == prime

## eratosthenes < N以下の全ての値の素数判定 >
1. 全てを素数と仮定
2. 0,1をfalseにする
3. 2..=Nでループ、trueであればその倍数の数字を全てfalseにする
4. trueの箇所が素数
