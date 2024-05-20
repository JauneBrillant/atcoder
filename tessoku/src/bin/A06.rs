use proconio::input;

fn main() {
    input! {
        n: usize,
        q: usize,
        a: [usize; n],
        lr: [(usize, usize); q],
    }

    let mut sums = vec![0; n + 1];
    let mut total = 0;
    for i in 1..=n {
        total += a[i - 1];
        sums[i] = total;
    }

    for (l, r) in lr {
        if l == 1 {
            println!("{}", sums[r]);
        } else {
            println!("{}", sums[r] - sums[l - 1]);
        }
    }
}
