use proconio::input;

fn main() {
    input! {
        n: usize,
        mut a: [usize; n],
    }

    a.sort();
    let missing_number = a.windows(2)
        .find_map(|window| {
            if window[1] - window[0] != 1 {
                Some(window[0] + 1)
            } else {
                None
            }
        });

    if let Some(res) = missing_number {
        println!("{}", res);
    }
}
