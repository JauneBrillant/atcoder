use proconio::input;

fn main() {
    input! {
        n: usize,
    }

    let mut res = 0;
    for i in 0..60 {
        if 2_usize.pow(i) <= n {
            res = i;
        }
    }

    println!("{}", res);
}
