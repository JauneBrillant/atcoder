use proconio::input;

fn main() {
    input! {
        n: usize,
        mut a: [usize; n],
    }

    a.sort();
    for window in a.windows(2) {
        if window[1] - window[0] != 1 {
            println!("{}", (window[0] + 1));
            return;
        }
    }
}
