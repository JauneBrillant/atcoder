use proconio::input;

fn main() {
    input! {
        n: usize,
    }

    println!("{}", if matches!(n, 2..=4) { "No" } else { "Yes" });
}
