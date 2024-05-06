use proconio::input;

fn main() {
    input! {
        s: String,
    }

    let str = "oxxoxxoxxoxxoxxoxxoxxoxxoxxoxxoxxo";
    for i in 0..3 {
        if s == str[i..i + s.len()] {
            println!("Yes");
            return;
        }
    }

    println!("No");
}
