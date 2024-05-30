use proconio::input;

fn main() {
    input! {
        r: usize,
        x: usize,
        y: usize,
    }

    let d2 = x * x + y * y;

    let mut ans = 1;
    loop {
        if r * r * ans * ans >= d2 {
            break;
        }
        ans += 1;
    }
    if ans == 1 && r * r > d2 {
        ans += 1;
    }

    println!("{}", ans);
}
