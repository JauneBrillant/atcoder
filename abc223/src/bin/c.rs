use proconio::input;

fn main() {
    input! {
        n: usize,
        ab: [(f64, f64); n],
    }

    let (mut li, mut ri) = (0, n - 1); // 現在端から何番目のマッチ棒か
    let (mut lx, mut rx) = (0.0, 0.0); // そのマッチ棒がどれくらい燃えているか
    let mut ans = 0.0;
    while li < ri {
        let lt = (ab[li].0 - lx) / ab[li].1; // 左が燃える時間を求める
        let rt = (ab[ri].0 - rx) / ab[ri].1;
        if lt < rt {
            ans += ab[li].1 * lt;
            lx = 0.0;
            rx += ab[ri].1 * lt;
            li += 1;
        } else {
            ans += ab[li].1 * rt;
            rx = 0.0;
            lx += ab[li].1 * rt;
            ri -= 1;
        }
    }
    ans += (ab[li].0 - lx - rx) / 2.0;

    println!("{ans}");
}
