use proconio::input;

fn main() {
    input! {
        h: i32,
    }

    let mut i = 1;
    while 2_i32.pow(i) - 1 <= h {
        i += 1;
    }

    println!("{}", i);
}
