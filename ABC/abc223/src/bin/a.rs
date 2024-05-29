use proconio::input;

fn main() {
    input! {
        x: usize
    }
    if x == 0 {
        println!("No");
        return;
    }

    let flag = x % 100 == 0;
    println!("{}", if flag { "Yes" } else { "No" });
}
