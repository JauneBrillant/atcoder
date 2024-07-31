use proconio::input;

fn main() {
    input! {
        n: usize,
        h: [usize; n],
    }

    let mut i = 0;
    while i < n - 1 && h[i] < h[i + 1] {
        i += 1;
    }

    println!("{}", h[i]);
}
