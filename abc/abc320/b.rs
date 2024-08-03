use proconio::input;
use std::collections::HashSet;

fn main() {
    input! {
        s: String,
    }

    let mut st = HashSet::new();
    for i in 0..s.len() {
        for j in i..=s.len() {
            st.insert(&s[i..j]);
        }
    }

    let res = st.iter()
        .filter(|e| is_palindrome(e))
        .map(|e| e.len())
        .max()
        .unwrap_or(0);

    println!("{}", res);
}

fn is_palindrome(str: &str) -> bool {
    str.chars().eq(str.chars().rev())
}
