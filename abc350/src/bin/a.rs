use proconio::input;

fn main() {
    input! {
        s: String,
    }

    let contest_num: i32 = s[3..].parse().unwrap();
    println!("{}", if contest_num != 0 && contest_num < 350 && contest_num != 316 { "Yes" } else { "No" });
}
