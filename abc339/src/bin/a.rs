use proconio::input;

fn main() {
    input! {
        s: String,
    }

    let mut index = 0;
    for (i, c) in s.chars().enumerate() {
        if c == '.' {
            index = i;
        }
    }

    println!("{}", &s[index + 1..])
}
