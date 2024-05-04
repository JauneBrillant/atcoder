use proconio::input;

fn main() {
    input! {
        _n: usize,
        x: usize,
        y: usize,
        z: usize,
    }

    let min = x.min(y);
    let max = y.max(x);
    println!("{}", if min <= z && z <= max { "Yes" } else { "No" });
}
