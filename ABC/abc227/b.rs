use proconio::input;
use std::collections::HashSet;

fn main() {
    input! {
        n: usize,
        s: [usize; n],
    }

    let mut st = HashSet::new();
    for a in 1..200 {
        for b in 1..200 {
            st.insert(4 * a * b + 3 * a + 3 * b);
        }
    }

    let mut res = 0;
    for v in s {
        if !st.contains(&v) {
            res += 1;
        }
    }

    println!("{}", res);
}
