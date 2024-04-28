use proconio::input;

fn main() {
    input! {
        n: usize,
        mut a: [usize; n],
    }

    a.sort();
    let mut res = 0;
    for i in 0..n - 1 {
        if a[i] + 1 != a[i + 1] {
            res = a[i] + 1;
        }
    }

    println!("{}", res);
}
