use proconio::input;

fn main() {
    input! {
        n: usize,
        k: usize,
        h: [i64; n],
    }

    let mut dp = vec![0; n];
    for i in 1..n {
        let mut min_cost = i64::MAX;
        let mut j: i64 = i as i64 - 1;
        let mut cnt = 0;
        while j >= 0 && cnt < k {
            let v = dp[j as usize] + (h[j as usize] - h[i]).abs();
            if v < min_cost {
                min_cost = v;
            }
            j -= 1;
            cnt += 1;
        }
        dp[i] = min_cost;
    }

    println!("{:?}", dp[n - 1]);
}
