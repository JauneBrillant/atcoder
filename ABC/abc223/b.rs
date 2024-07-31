use proconio::input;
use proconio::marker::Chars;
use std::collections::BTreeSet;

fn main() {
    input! {
        mut s: Chars,
    }

    let mut tree = BTreeSet::new();
    for _ in 0..s.len() {
        let tmp = s.pop().unwrap();
        s.insert(0, tmp);
        let new_str = s.iter().collect::<String>();
        tree.insert(new_str);
    }

    let res = tree.into_iter().collect::<Vec<String>>();
    println!("{}\n{}", res[0], res[res.len() - 1]);
}
