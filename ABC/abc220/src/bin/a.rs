use proconio::input;

fn main() {
    input! {
        a: i32,
        b: i32,
        c: i32,
    }

    let res = (a + c - 1) / c * c;
    // let res = ((a / c).ceil()) as i32 * c as i32;
    println!("{}", if res <= b { res } else { -1 });
}
