use proconio::input;
use std::collections::HashSet;

fn main() {
    input! {
        s1: String,
        s2: String,
        s3: String,
    }

    let mut set: HashSet<String> = vec!["ABC", "ARC", "AGC", "AHC"]
        .into_iter()
        .map(|s| s.to_string())
        .collect();

    set.remove(&s1);
    set.remove(&s2);
    set.remove(&s3);

    println!("{}", set.into_iter().next().unwrap());
}
