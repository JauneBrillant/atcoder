use proconio::input;
use std::collections::HashMap;

fn main() {
    input! {
        n: usize,
        s: [String; n],
    }

    let mut map = HashMap::new();
    for str in s {
        *map.entry(str).or_insert(0) += 1;
    }

    let res = map.iter().max_by_key(|&(_, v)| v).unwrap();
    println!("{}", res.0);
}
