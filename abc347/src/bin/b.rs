use proconio::input;
use std::collections::HashSet;

fn main() {
    input! {
        s: String,
    }

    let mut hashset: HashSet<&str> = HashSet::new();
    for i in 0..s.len() {
        for j in i+1..=s.len() {
            hashset.insert(&s[i..j]);
        }
    }

    println!{"{}", hashset.len()};
}
