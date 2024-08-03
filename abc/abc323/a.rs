use proconio::input;
use proconio::marker::Chars;

fn main() {
    input! {
        s: Chars,
    }

    let res = s.iter().enumerate().filter(|(i, _)| i % 2 != 0).all(|(_, &e)| e == '0');
    println!("{}", if res { "Yes" } else { "No" });
}
