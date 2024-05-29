use proconio::input;

fn main() {
    input! {
        n: usize,
        s: String,
    }

    let res = s.chars().nth(n - 1).unwrap() == 'o';
    println!("{}", if res { "Yes" } else { "No" });
}
