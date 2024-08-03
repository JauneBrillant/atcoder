use proconio::input;

fn main() {
    input! {
        s: String,
    }

    let res = s.chars().filter(|&c|
        c != 'a' &&
        c != 'i' &&
        c != 'u' &&
        c != 'e' &&
        c != 'o'
    ).collect::<String>();

    println!("{}", res);
}
