use proconio::input;

fn main() {
    input! {
        n: usize,
        cp: [(usize, usize); n],
        q: usize,
        lr: [(usize, usize); q],
    }

    let mut sum_a = 0;
    let mut sum_b = 0;
    let mut sums_a = vec![0; n + 1];
    let mut sums_b = vec![0; n + 1];

    for (i, (c, p)) in cp.into_iter().enumerate() {
        if c == 1 {
            sum_a += p;
        } else {
            sum_b += p;
        }
        sums_a[i + 1] = sum_a;
        sums_b[i + 1] = sum_b;
    }

    for (l, r) in lr.into_iter() {
        print!("{} ", sums_a[r] - sums_a[l - 1]);
        print!("{}\n", sums_b[r] - sums_b[l - 1]);
    }
}
