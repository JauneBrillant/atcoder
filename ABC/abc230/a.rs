use proconio::input;

fn main() {
    input! {
        n: usize,
    }
    if n < 10 {
        println!("AGC00{}", n);
    } else if n < 42 {
        println!("AGC0{}", n);
    } else {
        println!("AGC0{}", n + 1);
    }
}
