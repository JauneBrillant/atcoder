use proconio::input;

fn main() {
    input! {
        b: i64,
    }

    if let Some(i) = (1..=15 as i64).find(|&v| v.pow(v as u32) == b) {
        println!("{}", i);
    } else {
        println!("{}", -1);
    }
}
