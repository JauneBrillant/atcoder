use proconio::input;
use proconio::marker::Chars;

fn main() {
    input! {
        s: Chars,
    }

    const MOD: usize = 1_000_000_007;

    let t = "chokudai".chars().collect::<Vec<char>>();
    let m = t.len();
    let n = s.len();
    let mut dp = vec![vec![0; n + 1]; m + 1];

    for i in 0..=n {
        dp[0][i] = 1;
    }

    for i in 1..=m {
        for j in 1..=n {
            if t[i - 1] == s[j - 1] {
                dp[i][j] = (dp[i][j - 1] + dp[i - 1][j - 1]) % MOD;
            } else {
                dp[i][j] = dp[i][j - 1];
            }
        }
    }

    println!("{}", dp[8][n])
}
