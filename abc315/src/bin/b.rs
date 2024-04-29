use proconio::input;

fn main() {
    input! {
        m: usize,
        d: [usize; m],
    }

    let total_days = d.iter().sum::<usize>();
    let mut day = total_days / 2 + 1;

    let mut i = 0;
    while day > d[i] {
        day -= d[i];
        i += 1;
    }

    println!("{} {}", i + 1, day);
}
