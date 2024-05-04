use proconio::input;

fn main() {
    input! {
        s: String,
    }

    let len = s.len();
    println!("{}", if &s[len - 2..] == "er" { "er" } else { "ist" });
}
