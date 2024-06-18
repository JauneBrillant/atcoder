use proconio::input;

fn main() {
    input! {
        _n: usize,
        s: String,
    }

    let res = s.replace("na", "nya");
    println!("{}", res);
}
