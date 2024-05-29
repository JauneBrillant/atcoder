use proconio::input;

fn main() {
    input! {
        n: usize,
        p: [usize; n],
    }

    if n == 1 {
        println!("0");
        return;
    }

    let max = *p.iter().skip(1).max().unwrap();
    if p[0] > max {
        println!("0");
    } else {
        println!("{}", max - p[0] + 1);
    }
}
