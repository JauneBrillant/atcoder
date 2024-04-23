use proconio::input;

fn main() {
    input! {
        s: String,
    }

    let last_dot_index = s.rfind(|c: char| c == '.');
    println!("{}", &s[last_dot_index.unwrap() + 1..])
}
