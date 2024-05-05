use itertools::Itertools;
use proconio::input;
use proconio::marker::Chars;

fn main() {
    input! {
        s: Chars,
    }

    let res = s.iter().permutations(3).unique().count();
    println!("{}", res);
}
