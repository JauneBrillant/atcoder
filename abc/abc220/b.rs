use proconio::input;

fn main() {
    input! {
        k: u32,
        a: String,
        b: String,
    }

    let aa = usize::from_str_radix(&a, k).unwrap();
    let bb = usize::from_str_radix(&b, k).unwrap();

    let res = aa * bb;
    println!("{}", res);
}
