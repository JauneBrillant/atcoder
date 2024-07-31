use proconio::input;

fn main() {
    input! {
        n: usize,
        s: usize,
        m: usize,
        l: usize,
    }

    let mut res = usize::MAX;
    for i in 0..20 {
        for j in 0..20 {
            for k in 0..20 {
                if 6 * i + 8 * j + 12 * k >= n {
                    res = res.min(s * i + m * j + l * k);
                }
            }
        }
    }

    println!("{}", res);
}
