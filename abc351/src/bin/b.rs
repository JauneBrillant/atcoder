use proconio::input;

fn main() {
    input! {
        n: usize,
        grid_a: [String; n],
        grid_b: [String; n],
    }

    for i in 0..n {
        for j in 0..n {
            if grid_a[i].chars().nth(j) != grid_b[i].chars().nth(j) {
                println!("{} {}", i + 1, j + 1);
            }
        }
    }
}
