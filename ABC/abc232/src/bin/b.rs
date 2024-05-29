use proconio::input;
use proconio::marker::Chars;

fn main() {
    input! {
        s: Chars,
        t: Chars,
    }

    for k in 0..26 {
        let mut arr = vec![];
        for &c in s.iter() {
            let v = ((((c as u8 - b'a') as u8 + k) % 26) + b'a') as char;
            arr.push(v);
        }
        if arr == t {
            println!("Yes");
            return;
        }
    }

    println!("No");
}
