use proconio::input;

fn main() {
    input! {
        h: usize,
        w: usize,
    }

    let res = ((h + 1) / 2) * ((w + 1) / 2);
    if h == 1 || w == 1 {
        println!("{}", h * w);
    } else {
        println!("{}", res);
    }
}
