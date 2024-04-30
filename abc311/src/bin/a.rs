use proconio::input;
use proconio::marker::Chars;
use std::collections::HashSet;

fn main() {
    input! {
        _n: usize,
        s: Chars,
    }

    let mut st = HashSet::new();
    for (i, c) in s.iter().enumerate() {
        st.insert(c);
        if st.len() == 3 {
            println!("{}", i + 1);
            return;
        }
    }
}
