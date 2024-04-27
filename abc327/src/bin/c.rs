use proconio::input;
use std::collections::HashMap;

fn main() {
    input! {
        grid: [[usize; 9]; 9],
    }

    for i in 0..9 {
        let mut row_map = HashMap::new();
        let mut col_map = HashMap::new();
        for j in 0..9 {
            *row_map.entry(grid[i][j]).or_insert(0) += 1;
            *col_map.entry(grid[j][i]).or_insert(0) += 1;
        }
        if row_map.len() != 9 || col_map.len() != 9 {
            println!("No");
            return;
        }
     }

     for i in 0..3 {
         for j in 0..3 {
             let mut box_map = HashMap::new();
             let (a, b) = (i * 3, j * 3);
             for x in a..a + 3 {
                 for y in b..b + 3 {
                     *box_map.entry(grid[x][y]).or_insert(0) += 1;
                 }
             }
             if box_map.len() != 9 {
                 println!("No");
                 return;
             }
         }
     }

     println!("Yes");
}
