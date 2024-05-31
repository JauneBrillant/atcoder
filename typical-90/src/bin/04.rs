use proconio::input;

fn main() {
    input! {
        h: usize,
        w: usize,
        a: [[usize; w]; h],
    }

    let rows: Vec<usize> = a.iter().map(|vec| vec.iter().sum()).collect();
    let cols: Vec<usize> = (0..w).map(|j| a.iter().map(|row| row[j]).sum()).collect();

    for i in 0..h {
        for j in 0..w {
            print!("{} ", rows[i] + cols[j] - a[i][j]);
        }
        println!();
    }
}
