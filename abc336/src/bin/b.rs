use proconio::input;

fn main() {
    input! {
        n: i32,
    }

    let binary_string = format!("{:b}", n);
    let mut res = 0;
    for c in binary_string.chars().rev() {
        if c != '0' {
            break;
        }
        res += 1;
    }

    println!("{}", res);
}
