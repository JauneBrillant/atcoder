use proconio::input;

fn main() {
    input! {
        n: usize,
        k: usize,
        a: [usize; n],
    }

    let mut res = 0;

    let mut r = 1;
    for l in 0..n - 1 {
        while r < n && a[r] - a[l] <= k {
            r += 1;
        }
        res += r - l - 1;
    }

    println!("{}", res);
}
