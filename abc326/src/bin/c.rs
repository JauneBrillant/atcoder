use proconio::input;

fn main() {
    input! {
        n: usize,
        m: usize,
        mut a: [usize; n],
    }
    a.sort();

    let mut res = 0;
    let mut r = 0;
    for l in 0..n {
        while r < n && a[r as usize] < a[l] + m {
            r += 1;
        }
        res = res.max(r - l);
    }

    println!("{}", res);
}
