use proconio::input;

fn main() {
    input! {
        n: usize,
    }

    let str_n = n.to_string().trim_end_matches('0').to_string();
    let rev_str = str_n.chars().rev().collect::<String>();

    println!("{}", if str_n == rev_str { "Yes" } else { "No" });
}
