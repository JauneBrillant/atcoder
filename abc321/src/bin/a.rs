use proconio::input;
use proconio::marker::Chars;

fn main() {
    input! {
        n: Chars,
    }

    for i in 0..n.len() - 1 {
        if n[i] <= n[i + 1] {
            println!("No");
            return;
        }
    }

    println!("Yes");
}
