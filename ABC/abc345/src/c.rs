use proconio::input;
use proconio::marker::Chars;
use std::collections::HashMap;

fn main() {
    input! {
        s: Chars,
    }

    let mut map = HashMap::new();
    for c in s.iter() {
        *map.entry(c).or_insert(0) += 1;
    }

    let mut same = 0;
    for (_, cnt) in map {
        same += c2(cnt);
    }

    let mut res = c2(s.len()) - same;
    if same > 0 {
        res += 1;
    }
    println!("{}", res);
}

fn c2(n: usize) -> usize {
    n * (n - 1) / 2
}
