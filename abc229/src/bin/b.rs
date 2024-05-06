use proconio::input;

fn main() {
    input! {
        mut a: usize,
        mut b: usize,
    }

    while a > 0 && b > 0 {
        let a_digit = a % 10;
        let b_digit = b % 10;
        if a_digit + b_digit >= 10 {
            println!("Hard");
            return;
        }
        a /= 10;
        b /= 10;
    }

    println!("Easy");
}
