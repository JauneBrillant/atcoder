use proconio::input;

fn main() {
    input! {
        n: usize,
        m: usize,
        a: [usize; m],
        x: [[usize; m]; n],
    }

    let mut total = vec![0; m];
    for vec in x.into_iter() {
        for (i, v) in vec.into_iter().enumerate() {
            total[i] += v;
        }
    }

    let res = (0..m).all(|i| total[i] >= a[i]);
    println!("{}", if res { "Yes" } else { "No" });
}
