use proconio::input;

fn main() {
    input! {
        s: String,
        t: String,
    }

    let res = is_subarray(&(s.to_ascii_uppercase() + "X"), &t);
    println!("{}", if res { "Yes" } else { "No" });
}

fn is_subarray(s: &str, t: &str) -> bool {
    let mut t_index = 0;
    s.chars().any(|c| {
        if c == t.chars().nth(t_index).unwrap() {
            t_index += 1;
        }
        t_index == t.len()
    })
}
