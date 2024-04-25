use proconio::input;
use std::collections::BTreeSet;

fn main() {
    input! {
        n: usize,
    }

    let repunit: [i64; 12] = [
        1,
        11,
        111,
        1111,
        11111,
        111111,
        1111111,
        11111111,
        111111111,
        1111111111,
        11111111111,
        111111111111,
    ];

    let mut tree_map = BTreeSet::new();
    for i in repunit {
        for j in repunit {
            for k in repunit {
                tree_map.insert(i + j + k);
            }
        }
    }

    println!("{}", tree_map.iter().nth(n - 1).unwrap());
}
