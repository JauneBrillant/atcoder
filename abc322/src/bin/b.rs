use proconio::input;

fn main() {
    input! {
        _n: usize,
        _m: usize,
        s: String,
        t: String,
    }

    match (is_head(&s, &t), is_tail(&s, &t)) {
        (true, true) => println!("0"),
        (true, false) => println!("1"),
        (false, true) => println!("2"),
        _ => println!("3"),
    }
}

fn is_head(s: &str, t: &str) -> bool {
    t.starts_with(s)
}

fn is_tail(s: &str, t: &str) -> bool {
    t.ends_with(s)
}
