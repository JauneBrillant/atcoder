use proconio::input;

fn main() {
    input! {
        x: i32,
        y: i32,
    }

    let diff = y - x;
    println!("{}", if -3 <= diff && diff <= 2 { "Yes" } else { "No" });
}
