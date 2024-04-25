use proconio::input;
use std::collections::BTreeSet;

fn main() {
    input! {
        n: usize,
    }

    let repunit = generate_requnit();

    let mut tree_map = BTreeSet::new();
    for i in &repunit {
        for j in &repunit {
            for k in &repunit {
                tree_map.insert(i + j + k);
            }
        }
    }

    println!("{}", tree_map.iter().nth(n - 1).unwrap());
}

fn generate_requnit() -> Vec<i64> {
    let mut requnit: Vec<i64> = Vec::new();
    let mut value = 0;
    for _ in 0..12 {
        value = value * 10 + 1;
        requnit.push(value);
    }
    requnit
}
