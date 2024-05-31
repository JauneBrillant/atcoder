use proconio::input;

fn main() {
    input! {
        n: usize,
        k: i64,
        a: [i64; n],
        b: [i64; n],
    }

    let mut total_diff = 0;
    for i in 0..n {
        total_diff += (a[i] - b[i]).abs();
    }

    if total_diff <= k && (k - total_diff) % 2 == 0 {
        println!("Yes");
    } else {
        println!("No");
    }
}
