use proconio::input;

fn main() {
    input! {
        n: usize,
        l: usize,
        arr: [usize; n],
    }

    let mut res = 0;
    for &v in arr.iter() {
        if l <= v {
            res += 1;
        }
    }

    println!("{}", res);
}
