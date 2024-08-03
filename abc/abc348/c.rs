use proconio::input;
use std::collections::HashMap;

fn main() {
    input! {
        n: usize,
        beans: [(usize, usize); n],
    }

    let mut hashmap = HashMap::new();
    for (a, c) in beans {
        if let Some(&prev_a) = hashmap.get(&c) {
            if prev_a > a {
                hashmap.insert(c, a);
            }
        } else {
            hashmap.insert(c, a);
        }
    }

    let mut res = 0;
    for &v in hashmap.values() {
        if res < v {
            res = v;
        }
    }
    println!("{}", res);
}
