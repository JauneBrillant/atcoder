use proconio::input;

fn main() {
    input! {
        a: i64,
        b: i64,
        c: i64,
    }

    let res = c - (a - b);
    println!("{}", if res >= 0 { res } else { 0 });
}
