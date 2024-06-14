use proconio::input;

fn check(a: &Vec<usize>, x: usize, k: usize) -> bool {
    let mut sum = 0;
    for i in 0..a.len() {
        sum += x / a[i]
    }

    sum >= k
}

fn main() {
    input! {
        n: usize,
        k: usize,
        a: [usize; n],
    }

    let mut l = 0;
    let mut r = 100_000_000;
    while l < r {
        let m = (l + r) / 2;
        let ans = check(&a, m, k);
        if ans {
            r = m
        } else {
            l = m + 1;
        }
    }

    println!("{}", l);
}
