# Gretest Common Divisor

## 解法
- ユークリッドの互除法
1. 大きい方の数を「小さい方の数で割った余り」に変更するを繰り返す
2. 片方の数字がゼロになったら操作終了。もう一方の数が答え

## ①
```rust
use num::integer::gcd;

println!("{}", gcd(a, b));
```

## ②
```rust
fn gcd(mut x: usize, mut y: usize) {
  if y > x {
    let tmp = x;
    x = y;
    y = tmp;
  }

  if y == 0 {
    return x;
  }

  gcd(x % y, y)
}
```
