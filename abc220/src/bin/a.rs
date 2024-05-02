use proconio::input;

fn main() {
    input! {
        a: usize,
        b: usize,
        c: usize,
    }

    let mut res = -1;
    for i in a..=b {
        if i % c == 0 {
            res = i as i32;
        }
    }
    println!("{}", res);
}
