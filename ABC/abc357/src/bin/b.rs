use proconio::input;

fn main() {
    input! {
        mut s: String,
    }
    if s.len() == 1 {
        println!("{}", s);
        return;
    }

    let cnt_upper = s.chars().filter(|c| c.is_ascii_uppercase()).count();
    let cnt_lower = s.chars().filter(|c| c.is_ascii_lowercase()).count();

    let s = if cnt_upper > cnt_lower {
        s.to_uppercase()
    } else {
        s.to_lowercase()
    };

    println!("{}", s);
}
