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
    for c in s.chars() {
        if c == t.chars().nth(t_index).unwrap() {
            t_index += 1;
        }

        if t_index == t.len() {
            return true;
        }
    }
    false
}
