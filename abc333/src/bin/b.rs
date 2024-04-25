use proconio::input;

fn main() {
    input! {
        s: String,
        t: String,
    }

    let a = is_long(&s);
    let b = is_long(&t);

    println!("{}", if a == b { "Yes" } else { "No" });
}

fn is_long(s: &str) -> bool {
    let diff = (s.chars().nth(0).unwrap() as i32 - s.chars().nth(1).unwrap() as i32).abs();
    diff == 2 || diff == 3
}
