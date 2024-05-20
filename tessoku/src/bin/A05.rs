use proconio::input;

fn main() {
    input! {
        n: usize,
        k: usize,
    }

    let mut res = 0;
    for i in 1..=n {
        for j in 1..=n {
            let v = k - i - j;
            if 1 <= v && v <= n {
                res += 1;
            }
        }
    }

    println!("{}", res);
}
