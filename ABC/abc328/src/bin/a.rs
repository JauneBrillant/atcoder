use proconio::input;

fn main() {
    input! {
        n: usize,
        x: usize,
        s: [usize; n],
    }

    let res: usize = s.iter().filter(|&v| *v <= x).sum();
    println!("{}", res);
}
