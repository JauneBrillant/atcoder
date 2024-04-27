use proconio::input;
use proconio::marker::Chars;

fn main() {
    input! {
        _n: usize,
        a: Chars,
    }

    let res = a.windows(2).any(|pair| {
        pair[0] == 'a' && pair[1] == 'b' || pair[0] == 'b' && pair[1] == 'a'
    });

    println!("{}", if res { "Yes" } else { "No" });
}
