use proconio::input;

fn main() {
    input! {
        n: usize,
        xy: [(usize, usize); n],
    }

    let mut total_x = 0;
    let mut total_y = 0;
    for (x, y) in xy {
        total_x += x;
        total_y += y;
    }

    println!("{}", if total_x == total_y { "Draw" } else if total_x > total_y { "Takahashi" } else { "Aoki" });
}
