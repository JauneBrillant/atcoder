use proconio::input;
use std::collections::HashMap;

fn main() {
    input! {
        n: usize,
        q: usize,
        a: [usize; n],
        xk: [(usize, usize); q],
    }

    let mut hashmap = HashMap::new();
    for i in 0..n {
        hashmap.entry(a[i]).or_insert(vec![]).push(i + 1);
    }

    for &(x, k) in xk.iter() {
        if hashmap.contains_key(&x) && hashmap[&x].len() >= k {
            println!("{}", hashmap[&x][k - 1]);
        } else {
            println!("-1");
        }
    }
}
