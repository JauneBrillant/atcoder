use proconio::input;
use proconio::marker::Chars;

fn main() {
    input! {
        n: usize,
        m: usize,
        grid: [Chars; n],
    }

    let mut res = Vec::new();
    for i in 0..n - 8 {
        for j in 0..m - 8 {
            let square = grid[i..i + 9]
                .iter()
                .map(|row| row[j..j + 9].iter().cloned().collect())
                .collect::<Vec<Vec<char>>>();

            if is_tak_code(&square) {
                res.push((i, j));
            }
        }
    }

    for (i, j) in res {
        println!("{} {}", i + 1, j + 1);
    }
}

fn is_tak_code(grid: &Vec<Vec<char>>) -> bool {
    for i in 0..3 {
        for j in 0..3 {
            if grid[i][j] == '.' {
                return false;
            }

            if grid[8 - i][8 - j] == '.' {
                return false;
            }
        }
    }

    for i in 0..4 {
        if grid[i][3] == '#' {
            return false;
        }

        if grid[3][i] == '#' {
            return false;
        }

        if grid[8 - i][5] == '#' {
            return false;
        }

        if grid[5][8 - i] == '#' {
            return false;
        }
    }

    true
}
