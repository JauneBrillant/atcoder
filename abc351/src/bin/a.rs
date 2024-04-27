use proconio::input;

fn main() {
    input! {
        a: [usize; 9],
        b: [usize; 8],
    }

    let a_total: usize = a.iter().sum();
    let b_total: usize = b.iter().sum();

    println!("{}", a_total - b_total + 1);
}
