use proconio::input;

fn main() {
    input! {
        _n: usize,
        _m: usize,
        s: String,
        t: String,
    }

    if is_head(&s, &t) && is_tail(&s, &t) {
        println!("0");
    } else if is_head(&s, &t) && !is_tail(&s, &t) {
        println!("1");
    } else if !is_head(&s, &t) && is_tail(&s, &t) {
        println!("2");
    } else {
        println!("3");
    }
}

fn is_head(s: &str, t: &str) -> bool {
    *s == t[0..s.len()]
}

fn is_tail(s: &str, t: &str) -> bool {
    let l = t.len() - s.len();
    t[l..] == *s
}
