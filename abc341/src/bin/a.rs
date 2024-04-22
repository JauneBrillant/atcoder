use proconio::input;
use std::iter::repeat;

fn main() {
    input! {
        n: usize,
    }

    let res = repeat("10").take(n).collect::<String>() + "1";
    // let res = (0..n).map(|_| "10").collect::<String>() + "1";
    println!("{}", res);
}
