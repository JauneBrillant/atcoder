use proconio::input;

fn main() {
    input! {
        a: i32,
        b: i32,
    }

    match (a, 0 < a, b, 0 < b) {
        (_, true, 0, _) => println!("Gold"),
        (0, _, _, true) => println!("Silver"),
        (_, true, _, true) => println!("Alloy"),
        _ => unreachable!(),
    }
}
