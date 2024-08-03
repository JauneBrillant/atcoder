use proconio::input;

fn main() {
    input! {
        n: usize,
        h: [i64; n],
    }

    let mut dp = vec![0; n];
    dp[0] = 0;
    dp[1] = (h[0] - h[1]).abs();

    for i in 2..n {
        let one = dp[i - 1] + (h[i] - h[i - 1]).abs();
        let two = dp[i - 2] + (h[i] - h[i - 2]).abs();
        dp[i] = one.min(two);
    }

    println!("{}", dp[n - 1]);
}
