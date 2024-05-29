use proconio::input;

fn main() {
    input! {
        s: String,
    }

    if s.chars().nth(0).unwrap() != '<' || s.chars().nth(s.len() - 1).unwrap() != '>' {
        println!("No");
        return;
    }

    let cnt_equals = s.chars().filter(|&c| c == '=').count();

    println!("{}", if cnt_equals == s.len() - 2 { "Yes" } else { "No" })
}
