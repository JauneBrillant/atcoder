use proconio::input;
use std::collections::HashMap;

fn main() {
    input! {
        n: usize,
        p: [usize; n],
        q: usize,
        a: [(usize, usize); q],
    }

    let mut hashmap = HashMap::new();
    for (i, person) in p.iter().enumerate() {
        hashmap.insert(person, i);
    }

    for (first, second) in a {
        let res = hashmap.get(&first).min(hashmap.get(&second));
        println!("{:?}", p[*res.unwrap()]);
    }
}
