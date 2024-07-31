use itertools::Itertools;
use proconio::input;

fn main() {
    input! {
        n: usize,
        l: usize,
        r: usize,
    }

    let mut ans: Vec<usize> = (1..=n).collect();
    ans[l - 1..r].reverse();

    println!("{}", ans.iter().join(" "));
}
