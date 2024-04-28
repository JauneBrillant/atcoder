use proconio::input;

fn main() {
    input! {
        n: usize,
        a: [usize; n],
    }

    let res = a.iter().all(|&e| e == a[0]);
    println!("{}", if res { "Yes" } else { "No" });
}
