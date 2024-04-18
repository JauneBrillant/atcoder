use proconio::input;

fn main() {
    input! {
       n: usize,
       arr: [usize; n],
    }

    for i in 0..n-1 {
        println!("{} ", arr[i] * arr[i + 1]);
    }
}
