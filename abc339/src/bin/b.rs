use proconio::input;

fn main() {
    input! {
        h: usize,
        w: usize,
        n: usize,
    }

    let mut grid = vec![vec!['.'; w]; h];

    let mut current = (0, 0);
    let mut direction = 0;
    for i in 0..n {
        if grid[current.0][current.1] == '.'{
            grid[current.0][current.1] = '#';
            direction += 1;
        } else {
            grid[current.0][current.1] = '.';
            direction += 3;
        }

        direction %= 4;
        match direction {
            0 => current.0 = (current.0 + h - 1) % h, // 上
            1 => current.1 = (current.1 + 1) % w,     // 右
            2 => current.0 = (current.0 + 1) % h,     // 下
            3 => current.1 = (current.1 + w - 1) % w, // 左
            _ => unreachable!(),
        }
    }
    print_grid(&grid);
}

fn print_grid(grid: &Vec<Vec<char>>) {
    for row in grid {
        for item in row {
            print!("{}", item);
        }
        println!();
    }
}
