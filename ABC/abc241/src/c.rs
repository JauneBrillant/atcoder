use proconio::input;
use proconio::marker::Chars;

fn main() {
    input! {
        n: i32,
        s: [Chars; n],
    }

    let directions = [(0, 1), (1, 0), (1, 1), (-1, 1)];

    for i in 0..n {
        for j in 0..n {
            'outer: for (di, dj) in directions {
                let mut ni = i;
                let mut nj = j;
                let mut cnt = 0;

                for _ in 0..6 {
                    if ni < 0 || nj < 0 || ni >= n || nj >= n {
                        continue 'outer;
                    }
                    if s[ni as usize][nj as usize] == '.' {
                        cnt += 1;
                    }
                    ni += di;
                    nj += dj;
                }
                if cnt <= 2 {
                    println!("Yes");
                    return;
                }
            }
        }
    }

    println!("No");
}
