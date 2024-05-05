use proconio::input;

fn main() {
    input! {
        x: f64,
    }

    let res = x.round() as i64;
    println!("{}", res);
}
