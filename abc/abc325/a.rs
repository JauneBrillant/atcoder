use proconio::input;

fn main() {
    input! {
        s: String,
        _t: String,
    }

    let res = format!("{} san", s);
    println!("{}", res);
}
