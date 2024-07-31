use proconio::input;

fn main() {
    input! {
        a: u32,
        b: u32,
    }

    let res = a.pow(b) + b.pow(a);
    println!("{}", res);
}
