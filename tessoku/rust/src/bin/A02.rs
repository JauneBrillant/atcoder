use proconio::input;

fn main() {
    input! {
        n: usize,
        x: usize,
        a: [usize; n],
    }

    let res = a.iter().any(|&e| e == x);
    println!("{}", if res { "Yes" } else { "No" });
}
