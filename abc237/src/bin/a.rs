use proconio::input;

fn main() {
    input! {
        n: i64,
    }

    if -2_i64.pow(31) <= n && n <= (2_i64.pow(31) - 1) {
        println!("Yes");
    } else {
        println!("No");
    }
}
