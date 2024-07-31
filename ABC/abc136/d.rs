use proconio::input;
use proconio::marker::Chars;

fn main() {
    input! {
        s: Chars,
    }

    let n = s.len();

    let mut dp = vec![vec![0; n]; 33];
    for i in 0..n {
        if s[i] == 'R' {
            dp[0][i] = i + 1;
        } else {
            dp[0][i] = i - 1;
        }
    }

    for p in 0..32 {
        for i in 0..n {
            dp[p + 1][i] = dp[p][dp[p][i]];
        }
    }

    println!("{:?}", dp);

    let mut ans = vec![0; n];
    for i in 0..n {
        ans[dp[32][i]] += 1;
    }

    for v in ans {
        println!("{}", v);
    }
}
