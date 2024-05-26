use proconio::input;

fn main() {
    input! {
        a: usize,
        b: usize,
    }

    if a == b {
        println!("{}", -1);
    } else {
        match (a, b) {
            (1, 2) | (2, 1) => println!("3"),
            (2, 3) | (3, 2) => println!("1"),
            (1, 3) | (3, 1) => println!("2"),
            _ => (),
        }
    }
}
