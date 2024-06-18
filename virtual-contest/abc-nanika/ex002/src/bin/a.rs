use proconio::input;

fn main() {
    input! {
        a: i32,
        b: i32,
        c: i32,
        d: i32,

    }

    let res = a * d - b * c;
    println!("{}", res);
}
