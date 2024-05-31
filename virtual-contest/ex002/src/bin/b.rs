use proconio::input;

fn main() {
    input! {
        _n: usize,
        x: i64,
        s: String,
    }

    let res = s.chars().fold(x, |acc, c| {
        if c == 'o' {
            acc + 1
        } else if acc > 0 {
            acc - 1
        } else {
            acc
        }
    });

    println!("{}", res);
}
