use proconio::input;
use std::collections::HashMap;

fn main() {
    input! {
        n: usize,
    }

    let mut memo = HashMap::new();
    println!("{}", f(n, &mut memo));
}

fn f(x: usize, memo: &mut HashMap<usize, usize>) -> usize {
    if x == 1 {
        return 0;
    }

    if memo.contains_key(&x) {
        return memo[&x];
    }

    let res = f(x / 2, memo) + f((x + 1) / 2, memo) + x;
    memo.insert(x, res);
    res
}
