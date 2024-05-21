use proconio::input;

fn main() {
    input! {
        n: usize,
        k: usize,
        a: [usize; n],
    }

    let mut res = 0;
    let mut l = 0;
    for r in 1..n {
        while l < r && a[r] - a[l] > k {
            l += 1;
        }
        res += r - l;
    }

    println!("{}", res);
}
