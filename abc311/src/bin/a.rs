use proconio::input;
use proconio::marker::Chars;

fn main() {
    input! {
        _n: usize,
        s: Chars,
    }

    let mut cnt_a = false;
    let mut cnt_b = false;
    let mut cnt_c = false;
    for (i, c) in s.iter().enumerate() {
        match c {
            'A' => cnt_a = true,
            'B' => cnt_b = true,
            'C' => cnt_c = true,
            _ => (),
        }
        if cnt_a && cnt_b && cnt_c {
            println!("{}", i + 1);
            return;
        }
    }
}
