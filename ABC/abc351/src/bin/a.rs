use proconio::input;

fn main() {
    input! {
        a: [usize; 9],
        b: [usize; 8],
    }

    let a_total = a.iter().sum::<usize>();
    let b_total = b.iter().sum::<usize>();

    println!("{}", a_total - b_total + 1);
}
