use proconio::input;

fn main() {
    input! {
        a: [usize; 10],
    }

    let mut display_num = 0;
    for _ in 0..3 {
        display_num = a[display_num];
    }

    println!("{}", display_num);
}
