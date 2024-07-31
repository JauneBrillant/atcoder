use proconio::input;
use std::collections::HashMap;

fn main() {
    input! {
        n: usize,
        ab: [(usize, usize); n - 1],
    }

    let mut map = HashMap::new();
    for (a, b) in ab.iter() {
        *map.entry(a).or_insert(0) += 1;
        *map.entry(b).or_insert(0) += 1;
    }

    if let Some((_, v)) = map.into_iter().max_by_key(|&(_, cnt)| cnt) {
        if v == n - 1 {
            println!("Yes");
        } else {
            println!("No");
        }
    }
}
