use proconio::input;

fn main() {
    input! {
        h: usize,
        w: usize,
        x: [[usize; w]; h],
        q: usize,
        queries: [(usize, usize, usize, usize); q],
    }

    let mut grid = vec![vec![0; w + 1]; h + 1];
    for i in 1..=h {
        for j in 1..=w {
            grid[i][j] = grid[i][j - 1] + x[i - 1][j - 1];
        }
    }

    for i in 1..=w {
        for j in 1..=h {
            grid[j][i] += grid[j - 1][i];
        }
    }

    for (a, b, c, d) in queries {
        println!(
            "{}",
            grid[c][d] + grid[a - 1][b - 1] - grid[a - 1][d] - grid[c][b - 1]
        );
    }
}
