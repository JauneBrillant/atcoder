use proconio::input;

fn main() {
    input! {
        n: usize,
        mut w: usize,
        mut ab: [(usize, usize); n],
    }

    ab.sort_by(|(a1, _), (a2, _)| a2.cmp(a1));

    let mut res = 0;
    let mut i = 0;
    while w != 0 && i != ab.len() {
        if w >= ab[i].1 {
            w -= ab[i].1;
            res += ab[i].0 * ab[i].1;
        } else {
            while w != 0 {
                w -= 1;
                ab[i].1 -= 1;
                res += ab[i].0;
            }
        }
        i += 1;
    }

    println!("{}", res);
}
