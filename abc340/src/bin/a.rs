use proconio::input;

fn main() {
    input! {
        a: usize,
        b: usize,
        d: usize,
    }

    let mut num = a;
    while num <= b {
        print!("{}", num);
        if num == b { println!("\n") } else { print!(" ") };
        num += d;
    }
}
