use proconio::input;

fn main() {
    input! {
        n: usize,
        m: usize,
        h: [usize; n],
    }

    let ans = h
        .iter()
        .scan(0, |acc, x| {
            *acc += x;
            Some(*acc)
        })
        .position(|x| x > m)
        .unwrap_or(n);

    println!("{}", ans);
}
