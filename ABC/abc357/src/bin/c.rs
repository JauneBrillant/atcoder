use proconio::input;

fn main() {
    input! {
        n: u32,
    }

    let size = 3_usize.pow(n);
    let mut grid = vec![vec![' '; size]; size];

    println!("{:?}", grid);
}
