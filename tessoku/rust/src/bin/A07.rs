use proconio::input;

fn main() {
    input! {
        d: usize,
        n: usize,
        lr: [(usize, usize); n],
    }

    let mut days = vec![0; d];
    for (l, r) in lr {
        days[l - 1] += 1;
        if r == d {
            continue;
        }
        days[r] -= 1;
    }

    let mut total = 0;
    days.into_iter().for_each(|v| {
        total += v;
        println!("{}", total);
    });
}
