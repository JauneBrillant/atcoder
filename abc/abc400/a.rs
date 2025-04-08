use proconio::input;

fn main() {
    input! {
        a: i32
    }

    let b = if 400 % a == 0 { 400 / a } else { -1 };
    println!("{}", b)
}
