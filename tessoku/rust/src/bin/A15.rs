use proconio::input;

fn main() {
    input! {
        n: usize,
        a: [usize; n],
    }

    let mut b = vec![0; n];
    let mut aa = a.into_iter().enumerate().collect::<Vec<(usize, usize)>>();
    aa.sort_by_key(|&(_, v)| v);

    let mut num = 1;
    for i in 0..n - 1 {
        b[aa[i].0] = num;
        if aa[i].1 != aa[i + 1].1 {
            num += 1;
        }
    }
    b[aa[n - 1].0] = num;

    for v in b {
        print!("{} ", v);
    }
}
