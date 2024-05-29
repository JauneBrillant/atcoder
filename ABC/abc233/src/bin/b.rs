use proconio::input;

fn main() {
    input! {
        l: usize,
        r: usize,
        s: String,
    }

    let head = &s[0..l - 1];
    let mid = &s[l - 1..r].chars().rev().collect::<String>();
    let tail = &s[r..];

    let ss = format!("{}{}{}", head, mid, tail);
    println!("{}", ss);
}
