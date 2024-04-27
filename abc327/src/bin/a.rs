use proconio::input;
use proconio::marker::Chars;

fn main() {
    input! {
        n: usize,
        a: Chars,
    }

    for i in 0..n - 1 {
        if a[i] == 'a' && a[i + 1] == 'b' || a[i] == 'b' && a[i + 1] == 'a' {
            println!("Yes");
            return;
        }
    }
    println!("No")
}
