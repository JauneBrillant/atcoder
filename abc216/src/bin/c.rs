use proconio::input;

fn main() {
    input! {
        mut n: usize,
    }

    let mut res = String::from("");
    while n != 0 {
        if n % 2 == 0 {
            n /= 2;
            res += "B";
        } else {
            n -= 1;
            res += "A";
        }
    }

    println!("{}", res.chars().rev().collect::<String>());
}
