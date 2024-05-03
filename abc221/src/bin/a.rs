use proconio::input;

fn main() {
    input! {
        a: u32,
        b: u32,
    }

    let diff = a - b;
    println!("{}", 32_i32.pow(diff));
}
