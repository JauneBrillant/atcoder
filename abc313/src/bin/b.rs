use std::collections::HashSet;
use proconio::input;

fn main() {
    input! {
        n: usize,
        m: usize,
        ab: [(usize, usize); m],
    }

    let mut set = HashSet::new();
    for i in 1..=n {
        set.insert(i);
    }

    for (_, b) in ab.iter() {
        set.remove(b);
    }

    if set.len() >= 2 {
        println!("-1");
    } else {
        println!("{}", set.iter().nth(0).unwrap());
    }
}
