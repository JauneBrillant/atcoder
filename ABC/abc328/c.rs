use proconio::input;
use proconio::marker::Chars;

fn main() {
    input! {
        n: usize,
        q: usize,
        s: Chars,
        lr: [(usize, usize); q],
    }

    let mut a = vec![0; n - 1];
    for i in 0..n - 1 {
        a[i] = (s[i] == s[i + 1]) as usize;
    }

    let mut sum: Vec<usize> = vec![0; n];
    for i in 0..n - 1 {
        sum[i + 1] = sum[i] + a[i];
    }

    for i in 0..q {
        let (left, right) = lr[i];
        let res = sum[right - 1] - sum[left - 1];
        println!("{}", res);
    }
}
