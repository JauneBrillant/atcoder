use proconio::input;

fn main() {
    input! {
        n: i64,
    }

    let quinary = to_quinary(n - 1);
    println!("{}", quinary * 2);
}

fn to_quinary(mut n: i64) -> i64 {
    let mut res = 0;
    let mut base = 1;

    while n != 0 {
        let digit = n % 5;
        res += digit * base;
        n /= 5;
        base *= 10;
    }

    res
}
