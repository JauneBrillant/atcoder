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

    let mut res = usize::MIN;
    for e in st {
        if is_palindrome(e) {
            res = res.max(e.len());
        }
    }

    println!("{}", res);
}

fn is_palindrome(str: &str) -> bool {
    str.chars().eq(str.chars().rev())
}
