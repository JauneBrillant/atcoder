use proconio::input;
use proconio::marker::Chars;

fn main() {
    input! {
        n: Chars,
    }

    if n.windows(2).any(|w| w[0] <= w[1]) {
        println!("No");
    } else {
        println!("Yes");
    }
}
