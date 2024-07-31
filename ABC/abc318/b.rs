use proconio::input;

fn main() {
    input! {
        n: usize,
        m: [[usize; 4]; n],
    }

    let mut grid = vec![vec![false; 100]; 100];
    for points in m {
        let x1 = points[0];
        let x2 = points[1];
        let y1 = points[2];
        let y2 = points[3];

        for i in x1..x2 {
            for j in y1..y2 {
                grid[i][j] = true;
            }
        }
    }

    let res = grid.iter().flatten().filter(|&&e| e == true).count();
    println!("{}", res);
}
