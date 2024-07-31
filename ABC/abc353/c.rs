use proconio::input;

fn main() {
    input! {
        n: usize,
        a: [usize; n],
    }

    let mut sums = vec![];
    let mut sum = 0;
    for i in 0..n - 1 {
        sum += f(a[i], a[i + 1]);
        sums.push(sum);
    }

    println!("{:?}", sums);
}

fn f(x: usize, y: usize) -> i64 {
    ((x + y) % 100_000_000) as i64
}
