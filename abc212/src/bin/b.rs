use proconio::input;
use proconio::marker::Chars;

fn main() {
    input! {
        pass: Chars,
    }

    let is_all_same = pass.iter().all(|e| *e == pass[0]);
    let is_weak = pass.windows(2).all(|e| {
        e[0] == '9' && e[1] == '0' ||
        (e[0].to_digit(10).unwrap() + 1) == e[1].to_digit(10).unwrap()
    });

    if is_all_same || is_weak {
        println!("Weak");
    } else {
        println!("Strong");
    }
}
