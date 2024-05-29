use proconio::input;
use proconio::marker::Chars;

fn main() {
    input! {
        s: [String; 3],
        t: Chars,
    }

    let mut res = String::new();
    for idx in t {
        res += &s[idx.to_string().parse::<usize>().unwrap() - 1];
    }

    println!("{}", res);
}
