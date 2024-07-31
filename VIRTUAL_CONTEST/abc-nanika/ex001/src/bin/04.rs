use proconio::input;
use proconio::marker::Chars;
use std::collections::HashMap;

fn main() {
    input! {
        n: usize,
        k: usize,
        s: [Chars; n],
    }

    let mut res = 0;
    for i in 0..(1 << n) {
        let bit = format!("{:b}", i);
        let mut hashmap = HashMap::new();
        for (j, digit) in bit.chars().rev().enumerate() {
            if digit == '1' {
                for &c in s[j].iter() {
                    *hashmap.entry(c).or_insert(0) += 1;
                }
            }
        }
        let cnt = hashmap.values().filter(|&&v| v == k).count();
        res = res.max(cnt);
    }

    println!("{}", res);
}
