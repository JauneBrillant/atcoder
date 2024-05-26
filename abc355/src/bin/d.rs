use proconio::input;

fn main() {
    input! {
        n: usize,
    }

    let mut lr = vec![];
    for _ in 0..n {
        input! {
            l: usize,
            r: usize,
        }
        lr.push((l, 0));
        lr.push((r, 1));
    }

    lr.sort();

    let mut res = n * (n - 1) / 2;
    let mut r_cnt = 0;
    for (_, e_type) in lr {
        if e_type == 0 {
            res -= r_cnt;
        } else {
            r_cnt += 1;
        }
    }

    println!("{}", res);
}
