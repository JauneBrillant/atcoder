use proconio::input;

fn main() {
    input! {
        n: usize,
        x: usize,
        a: [usize; n],
    }

    let res = a.binary_search(&x);
    println!("{:?}", res.unwrap() + 1);
}
