use std::collections::BTreeMap;

use proconio::{input, marker::Chars};

fn main() {
    input! {
        n: usize,
        _m: usize,
        mut s: Chars,
        c: [usize; n]
    }

    let mut map = BTreeMap::new();
    for (i, c) in c.iter().enumerate() {
        map.entry(c).or_insert(vec![]).push(i);
    }

    for (_, arr) in map {
        if arr.len() < 2 { continue };

        let cp_s = s.clone();
        for i in 1..arr.len() {
            s[arr[i]] = cp_s[arr[i - 1]];
        }
        s[arr[0]] = cp_s[arr[arr.len() - 1]];
    }

    let res: String = s.iter().collect();
    println!("{}", res);
}
