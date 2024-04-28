use proconio::input;
use proconio::marker::Chars;

fn main() {
    input! {
        _n: usize,
        s: Chars,
    }

    for (i, window) in s.windows(3).enumerate() {
        if window == ['A', 'B', 'C'] {
            println!("{}", i + 1);
            return;
        }
    }
    println!("{}", -1);
}
