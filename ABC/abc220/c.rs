use proconio::input;

fn main() {
    input! {
        n: usize,
        a: [usize; n],
        x: usize,
    }

    let total_a = a.iter().sum::<usize>();
    let mut res = (x / total_a) * n;
    let mut total = total_a * (x / total_a);
    let mut i = 0;
    while total <= x {
        total += a[i];
        res += 1;
        i += 1;
    }

    println!("{}", res);
}
