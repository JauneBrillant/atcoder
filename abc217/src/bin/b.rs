use proconio::input;
use std::collections::HashSet;

fn main() {
    input! {
        s1: String,
        s2: String,
        s3: String,
    }

    let mut set = HashSet::new();
    set.insert(format!("{}", "ABC"));
    set.insert(format!("{}", "ARC"));
    set.insert(format!("{}", "AGC"));
    set.insert(format!("{}", "AHC"));

    set.remove(&s1);
    set.remove(&s2);
    set.remove(&s3);

    println!("{}", set.into_iter().next().unwrap());
}
