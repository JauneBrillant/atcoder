use proconio::input;

fn main() {
    input! {
        n: usize,
        mut m: usize,
        p: usize,
    }

    let mut res = 0;
    while m <= n {
        res += 1;
        m += p;
    }

    println!("{}", res);
}
