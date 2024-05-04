use proconio::input;

fn main() {
    input! {
        n: usize,
        ab: [(usize, usize); n],
    }

    let mut res = 0;
    let total = ab.iter().map(|(a, _)| a).sum::<usize>();
    for (a, b) in ab.iter() {
        res = res.max(total - a + b);
    }

    println!("{}", res);
}
