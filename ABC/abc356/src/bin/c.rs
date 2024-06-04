use itertools::Itertools;
use proconio::input;
use proconio::marker::Usize1;

fn main() {
    input! {
        n: usize,
        m: usize,
        k: u32,
    }

    let trials = (0..m)
        .map(|_| {
            input! {
                c: usize,
                a: [Usize1; c],
                r: char,
            }
            let a = a.iter().fold(0, |acc, &x| acc | 1 << x);
            (a, r == 'o')
        })
        .collect_vec();

    let ans = (0u32..(1 << n))
        .filter(|bs| {
            trials
                .iter()
                .all(|&(a, r)| r == ((a & bs).count_ones() >= k))
        })
        .count();

    println!("{}", ans);
}
