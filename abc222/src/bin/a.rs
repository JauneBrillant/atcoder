use proconio::input;
use proconio::marker::Chars;

fn main() {
    input! {
        mut n: Chars,
    }

    for _ in 0..4 - n.len() {
        n.insert(0, '0');
    }

    println!("{}", n.iter().collect::<String>());
}
