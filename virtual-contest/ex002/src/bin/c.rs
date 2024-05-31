use proconio::input;

fn main() {
    input! {
        a: i64,
        b: i64,
        c: i64,
        d: i64,
    }

    let res;
    if a == c && b == d {
        res = 0;
    } else if a + b == c + d || a - b == c - d || (a - c).abs() + (b - d).abs() <= 3 {
        res = 1;
    } else if (a + b) % 2 == (c + d) % 2 || (b - d).abs() <= 2 {
        res = 2;
    } else {
        res = 3;
    }

    println!("{}", res);
}
