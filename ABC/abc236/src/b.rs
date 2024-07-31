use proconio::input;
use std::collections::HashMap;

fn main() {
    input! {
        n: usize,
        a: [usize; (4 * n) - 1],
    }

    let mut map = HashMap::new();
    for v in a {
        *map.entry(v).or_insert(0) += 1;
    }

    for (k, v) in map {
        if v == 3 {
            println!("{}", k);
            return;
        }
    }
}
