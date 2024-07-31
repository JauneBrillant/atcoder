use proconio::input;

fn main() {
    input! {
        x: i64,
    }

    let res = if x >= 0 { (x + 10 - 1) / 10 } else { x / 10 };
    println!("{}", res);
}

// 切り上げ除算
// (a + b - 1) / b
