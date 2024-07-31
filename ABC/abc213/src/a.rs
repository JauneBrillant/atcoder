use proconio::input;

fn main() {
    input! {
        a: usize,
        b: usize,
    }

    let c = a ^ b;
    println!("{}", c);
}
