use proconio::input;

fn main() {
    input! {
        mut n: usize,
    }

    let mut res = String::from("");
    while n != 0 {
        if n & 1 == 0 {
            n >>= 1;
            res += "B";
        } else {
            n -= 1;
            n >>= 1;
            res += "AB";
        }
    }

    println!("{}", res.chars().rev().collect::<String>());
}
