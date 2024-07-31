use proconio::input;

fn main() {
    input! {
        a: usize,
        b: usize,
    }

    let res = (a..=b).any(|i| 100 % i == 0);
    println!("{}", if res { "Yes" } else { "No" });
}
