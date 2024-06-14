use proconio::input;

fn main() {
    input! {
        n: usize,
        a: [usize; n],
        d: usize,
        lr: [(usize, usize); d],
    }

    let mut lr_sum = vec![0; n + 2];
    for i in 1..=n {
        lr_sum[i] = lr_sum[i - 1].max(a[i - 1]);
    }

    let mut rl_sum = vec![0; n + 2];
    for i in (1..=n).rev() {
        rl_sum[i] = rl_sum[i + 1].max(a[i - 1]);
    }

    for (l, r) in lr {
        let res = lr_sum[l - 1].max(rl_sum[r + 1]);
        println!("{}", res);
    }
}
