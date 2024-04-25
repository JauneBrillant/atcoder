use proconio::input;

fn main() {
    input! {
        n: usize,
    }

    let res: String = (0..n).map(|_| n.to_string()).collect();
    println!("{}", res);
}
