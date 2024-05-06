use proconio::input;

fn main() {
    input! {
        x: usize,
        y: usize,
    }

    if x >= y {
        println!("0");
    } else {
        let diff = y - x;
        if diff % 10 == 0 {
            println!("{}", diff / 10);
        } else {
            println!("{}", (diff / 10) + 1);
        }
    }
}
