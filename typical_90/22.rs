use num::integer::gcd;
use proconio::input;

fn main() {
    input! {
        mut a: usize,
        mut b: usize,
        mut c: usize,
    }

    let gcd = gcd(gcd(a, b), c);
    let res = a / gcd - 1 + b / gcd - 1 + c / gcd - 1;
    println!("{}", res);
}
