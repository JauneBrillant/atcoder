use proconio::input;
use proconio::marker::Chars;

fn main() {
    input! {
        n: usize,
        d: usize,
        s: [Chars; n],
    }

    let mut res = 0;
    let mut streak = 0;
    for i in 0..d {
        for j in 0..n {
            if s[j][i] == 'x' {
                streak = 0;
                break;
            }
            if j == n - 1 {
                streak += 1;
            }
        }
        res = res.max(streak);
    }

    println!("{}", res);
}
