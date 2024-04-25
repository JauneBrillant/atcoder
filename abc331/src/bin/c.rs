use proconio::input;

fn main() {
    input! {
        n: usize,
        a: [usize; n],
    }
    let m = 1_000_009;

    let mut arr: Vec<Vec<usize>> = vec![vec![]; m];
    for (i, &num) in a.iter().enumerate() {
        arr[num].push(i);
    }

    let mut res: Vec<usize> = vec![0; n];
    let mut total = 0;
    for i in (0..m).rev() {
        for j in 0..arr[i].len() {
            res[arr[i][j]] = total;
        }
        total += i * arr[i].len();
    }

    for v in res {
        print!("{} ", v);
    }
}
