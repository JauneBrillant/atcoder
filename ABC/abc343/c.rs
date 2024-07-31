use proconio::input;

fn main() {
    input! {
        n: i64,
    }

    let mut res = 0;
    for num in 1..=n {
        let cube = num.pow(3);
        if cube > n {
            break;
        }

        if is_palindrome(cube) {
            res = cube;
        }
    }
    println!("{}", res);
}

fn is_palindrome(num: i64) -> bool {
    let s: String = num.to_string();
    let rev_s: String = s.chars().rev().collect();
    s == rev_s
}
