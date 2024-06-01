use proconio::input;
use proconio::marker::Chars;

fn main() {
    input! {
        x: usize,
        y: usize,
        z: usize,
        s: Chars,
    }

    let n = s.len();
    let mut dp = vec![vec![0; n + 1]; 2];
}
