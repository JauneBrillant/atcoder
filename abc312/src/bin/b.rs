use proconio::input;
use proconio::marker::Chars;

fn main() {
    input! {
        n: usize,
        m: usize,
        grid: [Chars; n],
    }

    let mut res = vec![];
    for i in 0..(n - 8) {
        for j in 0..(m - 8) {
            let mut square: Vec<Vec<char>> = vec![];
            for k in 0..9 {
                square.push(grid[i + k][j..(j + 9)].to_vec());
            }

            if check(&square) {
                res.push((i + 1, j + 1));
            }
        }
    }

    for (i, j) in res {
        println!("{} {}", i, j);
    }
}

fn check(grid: &[Vec<char>]) -> bool {
    for i in 0..3 {
        for j in 0..3 {
            if grid[i][j] != '#' {
                return false;
            }
        }
    }

    for i in 0..3 {
        for j in 0..3 {
            if grid[8 - i][8 - j] != '#' {
                return false
            }
        }
    }

    for i in 0..4 {
        for j in 0..4 {
            if i < 3 && j < 3 {
                continue;
            }

            if grid[i][j] != '.' {
                return false;
            }
        }
    }

    for i in 0..4 {
        for j in 0..4 {
            if i < 3 && j < 3 {
                continue;
            }

            if grid[8 - i][8 - j] != '.' {
                return false;
            }
        }
    }
    true
}
