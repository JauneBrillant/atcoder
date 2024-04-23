use proconio::input;

fn main() {
    input! {
        n: i32,
    }

    let binary_string = format!("{:b}", n);
    let res = binary_string.chars()
        .rev()
        .take_while(|&c| c == '0')
        .count();

    println!("{}", res);
}
