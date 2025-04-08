use proconio::input;

fn main() {
    input! {
        n: usize,
        m: usize,
    }

    const LIMIT: usize = 1_000_000_000;

    let sum = (0..=m)
        .map(|i| n.saturating_pow(i as u32))
        .try_fold(0usize, |acc, v| acc.checked_add(v).filter(|&n| n <= LIMIT));

    match sum {
        Some(v) => println!("{}", v),
        None => println!("inf"),
    }
}
