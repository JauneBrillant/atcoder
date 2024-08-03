use proconio::input;

fn main() {
    input! {
        n: usize,
        mut h: [usize; n],
    }

    for i in 0..n - 1 {
        if h[i] < h[i + 1] {
            h[i + 1] -= 1;
        }
    }

    let res = h.windows(2).all(|win| win[0] <= win[1]);

    println!("{}", if res { "Yes" } else { "No" });
}
