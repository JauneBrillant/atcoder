use proconio::input;

fn main() {
    input! {
        h: usize,
        w: usize,
        n: usize,
        q: [(usize, usize, usize, usize); n],
    }

    let mut grid = vec![vec![0; w + 2]; h + 2];
    for (a, b, c, d) in q {
        grid[a][b] += 1;
        grid[c + 1][d + 1] += 1;
        grid[c + 1][b] -= 1;
        grid[a][d + 1] -= 1;
    }

    for i in 1..=h {
        for j in 1..w {
            grid[i][j + 1] += grid[i][j];
        }
    }

    for i in 1..=w {
        for j in 1..h {
            grid[j + 1][i] += grid[j][i];
        }
    }

    for i in 1..=h {
        for j in 1..=w {
            print!("{} ", grid[i][j]);
        }
        println!();
    }
}
