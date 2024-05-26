use proconio::input;

fn main() {
    input! {
        n: usize,
        t: usize,
        a: [usize; t],
    }

    let mut grid = vec![vec![false; n]; n];
    let mut row_cnt = vec![0; n];
    let mut col_cnt = vec![0; n];
    let mut diagonal1 = 0;
    let mut diagonal2 = 0;

    for (i, v) in a.iter().enumerate() {
        let row = (v - 1) / n;
        let col = (v - 1) % n;
        grid[row][col] = true;

        row_cnt[row] += 1;
        col_cnt[col] += 1;

        if row == col {
            diagonal1 += 1;
        }

        if row + col == n - 1 {
            diagonal2 += 1;
        }

        if row_cnt[row] == n || col_cnt[col] == n || diagonal1 == n || diagonal2 == n {
            println!("{}", i + 1);
            return;
        }
    }

    println!("-1");
}
