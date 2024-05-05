use proconio::input;

fn main() {
    input! {
        s: usize,
        t: usize,
        x: usize,
    }

    if s < t {
        println!("{}", if s <= x && x < t { "Yes" } else { "No" });
    } else {
        println!("{}", if t <= x && x < s { "No" } else { "Yes" });
    }
}
