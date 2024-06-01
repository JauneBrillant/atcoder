use proconio::input;
use std::collections::HashSet;

fn main() {
    input! {
        n: usize,
        s: [String; n],
    }

    let mut set = HashSet::new();
    for (i, str) in s.into_iter().enumerate() {
        if set.insert(str) {
            println!("{}", i + 1);
        }
    }
}
