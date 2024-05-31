use proconio::input;

fn main() {
    input! {
        h: usize,
        w: usize,
        a: [[usize; w]; h],
    }

    let mut rows = vec![0; h];
    let mut cols = vec![0; w];
    for i in 0..h {
        for j in 0..w {
            rows[i] += a[i][j];
            cols[j] += a[i][j];
        }
    }

    for i in 0..h {
        for j in 0..w {
            print!("{} ", rows[i] + cols[j] - a[i][j]);
        }
        println!();
    }
}
