use proconio::input;
use proconio::marker::Chars;

fn main() {
    input! {
        n: usize,
        a: [Chars; n],
    }

    let res = rotate(&a, n);

    for row in res {
        let str = row.iter().collect::<String>();
        println!("{}", str);
    }
}

fn rotate(a: &Vec<Vec<char>>, n: usize) -> Vec<Vec<char>> {
    let mut b = vec![vec!['0'; a[0].len()]; a.len()];
    for i in 0..a.len() {
        for j in 0..a[i].len() {
            b[i][j] = a[i][j];
        }
    }

    let mut arr = vec![];
    for i in 0..n - 1 { arr.push((0, i)) }
    for i in 0..n - 1 { arr.push((i, n - 1)) }
    for i in (1..n).rev() { arr.push((n - 1, i)) }
    for i in (1..n).rev() { arr.push((i, 0)) }

    let size = arr.len();
    let mut cp_arr = arr.clone();
    for i in 0..size {
        if i == 0 {
            cp_arr[0] = cp_arr[size - 1];
        } else {
            cp_arr[i] = arr[i - 1];
        }
    }

    for i in 0..size {
        b[arr[i].0][arr[i].1] = a[cp_arr[i].0][cp_arr[i].1];
    }

    b
}
