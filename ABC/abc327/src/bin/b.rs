use proconio::input;

fn main() {
    input! {
        b: i64,
    }

    if let Some(res) = (1..16 as i64).find(|&v| v.pow(v as u32) == b) {
        println!("{}", res);
    } else {
        println!("{}", -1);
    }
}
