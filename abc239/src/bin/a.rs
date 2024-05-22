use proconio::input;

fn main() {
    input! {
        h: f64,
    }

    let res = (h * (12800000.0 + h)).sqrt();
    println!("{}", res);
}
