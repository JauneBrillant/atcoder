use proconio::input;
// use std::iter::*;

fn main() {
    input! {
        n: usize,
    }

    // let res: String = once('L')
    //     .chain(repeat('o').take(n))
    //     .chain(once('n'))
    //     .chain(once('g'))
    //     .collect();

    let res = format!("L{}ng", "o".repeat(n));
    println!("{}", res);
}
