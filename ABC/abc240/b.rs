use proconio::input;
use std::collections::HashSet;

fn main() {
    input! {
        n: usize,
        a: [usize; n],
    }

    let st: HashSet<usize> = a.into_iter().collect();
    println!("{}", st.len());
}
