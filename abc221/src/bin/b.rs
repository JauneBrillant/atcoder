use proconio::input;
use proconio::marker::Chars;

fn main() {
    input! {
        s: Chars,
        t: Chars,
    }
    if s == t { println!("Yes"); return}

    for i in 0..s.len() - 1 {
        let mut s_copy = s.clone();
        s_copy.swap(i, i + 1);

        if s_copy == t {
            println!("Yes");
            return;
        }
    }

    println!("No");
}
