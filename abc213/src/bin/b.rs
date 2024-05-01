use proconio::input;
use std::collections::HashMap;

fn main() {
    input! {
        n: usize,
        a: [usize; n],
    }

    let mut map = HashMap::new();
    for (i, v) in a.iter().enumerate() {
        map.insert(v, i + 1);
    }

    let mut sorted_keys = map.keys().collect::<Vec<_>>();
    sorted_keys.sort_by(|a, b| b.cmp(a));

    let res = map.get(sorted_keys[1]).unwrap();
    println!("{}", res);
}
