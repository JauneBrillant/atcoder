use proconio::input;
use std::collections::HashSet;

fn main() {
    input! {
        n: usize,
        st: [(String, String); n],
    }

    let mut set = HashSet::new();
    for name in st.iter() {
        if set.contains(name) {
            println!("Yes");
            return;
        }
        set.insert(name);
    }
    println!("No");
}
