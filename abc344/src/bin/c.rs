use proconio::input;
use std::collections::HashSet;

fn main() {
    input! {
        n: usize,
        a: [i64; n],
        m: usize,
        b: [i64; m],
        l: usize,
        c: [i64; l],
        q: usize,
        x: [i64; q],
    }

    let mut set = HashSet::new();
    for ai in a.iter() {
        for bj in b.iter() {
            for ck in c.iter() {
                set.insert(ai + bj + ck);
            }
        }
    }

    for num in x {
        println!("{}", if set.contains(&num) { "Yes" } else { "No" });
    }
}
