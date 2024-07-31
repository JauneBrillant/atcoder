use proconio::input;
use proconio::marker::Chars;
use std::collections::VecDeque;

fn main() {
    input! {
        h: usize,
        w: usize,
        grid: [Chars; h],
    }

    let mut max_freedom = 0;
    for i in 0..h {
        for j in 0..w {
            if grid[i][j] == '.' {
                max_freedom = max_freedom.max(calc_freedom(&grid, i, j));
            }
        }
    }
    println!("{}", max_freedom);
}

fn calc_freedom(grid: &Vec<Vec<char>>, i: usize, j: usize) -> usize {
    let mut visited = vec![vec![false; grid[0].len()]; grid.len()];
    let mut queue = VecDeque::new();
    queue.push_back((i, j));
    visited[i][j] = true;
    let mut freedom = 0; // 自由度を 0 からスタートする

    let dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)];

    while let Some((r, c)) = queue.pop_front() {
        for &(dr, dc) in &dirs {
            let nr = (r as i32 + dr) as usize;
            let nc = (c as i32 + dc) as usize;
            if nr < grid.len() && nc < grid[0].len() && grid[nr][nc] == '.' && !visited[nr][nc] {
                queue.push_back((nr, nc));
                visited[nr][nc] = true;
                freedom += 1;
            }
        }
    }

    freedom
}
