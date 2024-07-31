use proconio::input;
use proconio::marker::Chars;

fn main() {
    input! {
        s: Chars,
        t: Chars,
    }

    println!("{}", if s < t { "Yes" } else { "No" });
}
