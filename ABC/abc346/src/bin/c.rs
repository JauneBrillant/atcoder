use proconio::input;
use std::collections::HashSet;

fn main() {
    input! {
        n: usize,
        k: i64,
        arr: [i64; n],
    }

    let mut st = HashSet::new();
    for &num in arr.iter() {
        if num <= k {
            st.insert(num);
        }
    }

    let total: i64 = k * (k + 1) / 2;
    let res = total - st.iter().sum::<i64>();
    println!("{}", res);
}
