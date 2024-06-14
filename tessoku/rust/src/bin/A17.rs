use proconio::input;

fn main() {
    input! {
        n: usize,
        a: [usize; n - 1],
        b: [usize; n - 2],
    }

    let mut dp = vec![0; n];
    dp[0] = 0;
    dp[1] = a[0];
    for i in 2..n {
        dp[i] = (dp[i - 1] + a[i - 1]).min(dp[i - 2] + b[i - 2]);
    }

    let mut res = vec![];
    let mut curr = n;
    loop {
        res.push(curr);
        if curr == 1 {
            break;
        }

        if dp[curr - 2] + a[curr - 2] == dp[curr - 1] {
            curr -= 1;
        } else {
            curr -= 2;
        }
    }

    println!("{}", res.len());
    for v in res.iter().rev() {
        print!("{} ", v);
    }
}
