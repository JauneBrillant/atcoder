use proconio::input;

fn main() {
    input! {
        mut k: usize,
        g: i32,
        m: i32,
    }

    let mut glass = 0;
    let mut cup = 0;
    while k > 0 {
        if glass == g {
            glass = 0;
        } else if cup == 0 {
            cup = m;
        } else {
            // マグカップからグラスに水を移す
            // グラスの残り容量 = グラスの最大容量 - 今のグラスの容量
            let diff = g - glass;
            if diff < cup {
                glass += diff;
                cup -= diff;
            } else {
                // 全て注ぐ時
                glass += cup;
                cup = 0;
            }
        }
        k -= 1;
    }

    println!("{} {}", glass, cup);
}
