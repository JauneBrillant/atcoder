use proconio::input;
use proconio::marker::*;

fn main() {
    input! {
        s: Bytes,
        t: Bytes,
    }

    let is_long = |s: Vec<u8>| -> bool {
        let diff = (s[0] as i32 - s[1] as i32).abs();
        diff == 1 || diff == 4
    };

    let a = is_long(s);
    let b = is_long(t);

    println!("{}", if a == b { "Yes" } else { "No" });
}
