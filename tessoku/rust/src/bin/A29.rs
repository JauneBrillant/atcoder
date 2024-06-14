use proconio::input;

fn main() {
    input! {
        a: usize,
        b: usize,
    }

    println!("{}", power(a, b, 1000_000_007));
}

fn power(a: usize, mut b: usize, m: usize) -> usize {
    let mut base = a;
    let mut res = 1;

    while b > 0 {
        if b % 2 == 1 {
            res *= base;
            res %= m;
        }
        base *= base;
        base %= m;
        b /= 2;
    }

    res
}
