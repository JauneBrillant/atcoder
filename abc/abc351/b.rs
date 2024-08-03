use proconio::input;
use proconio::marker::Chars;

fn main() {
    input! {
        n: usize,
        grid_a: [Chars; n],
        grid_b: [Chars; n],
    }

    for i in 0..n {
        for j in 0..n {
            if grid_a[i][j] != grid_b[i][j] {
                println!("{} {}", i + 1, j + 1);
                return;
            }
        }
    }
    unreachable!();
}
