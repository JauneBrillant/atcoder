use proconio::input;

fn main() {
    input! {
        s: String,
    }

    let str = "oxxoxxoxxoxxoxxoxxoxxoxxoxxoxxoxxo";
    if str.contains(&s) {
        println!("Yes")
    } else {
        println!("No");
    }
}
