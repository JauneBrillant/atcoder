use proconio::input;

fn main() {
    input! {
        t: usize,
    }
    let res = f(f(f(t) + t) + f(f(t)));
    println!("{}", res);
}

fn f(x: usize) -> usize {
    x * x + 2 * x + 3
}
