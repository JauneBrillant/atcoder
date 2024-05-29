use proconio::input;

fn main() {
    input! {
        a: usize,
        b: usize,
    }

    match (a, b) {
        (1, 2) | (2, 3) | (4, 5) | (5, 6) | (7, 8) | (8, 9) => println!("Yes"),
        (_, _) => println!("No"),
    }
}
