use proconio::{input, marker::Chars};

fn main() {
    input! {
        h: usize,
        w: usize,
        n: usize,
        t: Chars,
        s: [Chars; h],
    }

    let mut res = 0;
    for i in 0..h {
        'next: for j in 0..w {
            if s[i][j] == '#' {
                continue;
            }

            let mut curr_i = i;
            let mut curr_j = j;
            for c in t.iter() {
                match c {
                    'L' => curr_j -= 1,
                    'R' => curr_j += 1,
                    'U' => curr_i -= 1,
                    'D' => curr_i += 1,
                    _ => (),
                }
                if s[curr_i][curr_j] == '#' {
                    continue 'next;
                }
            }
            res += 1;
        }
    }

    println!("{}", res);
}
