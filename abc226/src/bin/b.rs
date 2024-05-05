use proconio::input;
use std::collections::HashSet;

fn main() {
    input! {
        n: usize,
    }

    let mut st = HashSet::new();

    for _ in 0..n {
        input! {
            l: usize,
            a: [usize; l],
        }
        st.insert(a);
    }

    println!("{}", st.len())
}
