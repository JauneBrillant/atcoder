use proconio::input;

fn main() {
    input! {
        n: u8,
        s: String,
    }

    let res = s
        .bytes()
        .map(|c| (((c - b'A' + n) % 26) + b'A') as char)
        .collect::<String>();

    println!("{}", res);
}
